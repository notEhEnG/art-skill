#!/usr/bin/env python3
"""Copy the portable skill into explicit project-local agent directories."""

import argparse
import errno
import json
import shutil
import sys
from pathlib import Path

ROOTS = {"codex": ".agents", "claude": ".claude", "cursor": ".cursor"}
SOURCE = Path(__file__).resolve().parents[1] / "skills" / "art-skill"


def destinations(project, agents):
    project = Path(project).resolve()
    if not project.is_dir():
        raise ValueError("project must be an existing directory")
    result = []
    for agent in dict.fromkeys(agents):
        target = project / ROOTS[agent] / "skills" / "art-skill"
        if not target.resolve().is_relative_to(project):
            raise ValueError(f"target resolves outside project: {target}")
        if target.exists() or target.is_symlink():
            raise ValueError(f"target already exists; keep it or choose another project: {target}")
        result.append((agent, target))
    return result


def install_targets(project, targets):
    """Roll back this invocation's copies on failure; preserve existing content."""
    project = Path(project).resolve()
    created_targets, created_parents = [], []
    try:
        for _, target in targets:
            missing, parent = [], target.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for parent in reversed(missing):
                try:
                    parent.mkdir()
                except FileExistsError:
                    if not parent.is_dir():
                        raise
                else:
                    created_parents.append(parent)
            if not target.resolve().is_relative_to(project):
                raise ValueError(f"target resolves outside project: {target}")
            # Claim the target exclusively so a newly appeared installation is
            # never copied into or added to our rollback list.
            target.mkdir()
            created_targets.append(target)
            shutil.copytree(
                SOURCE, target, dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
    except BaseException as exc:
        cleanup_errors = []
        for target in reversed(created_targets):
            try:
                if not target.resolve().is_relative_to(project):
                    raise OSError(f"refusing rollback outside project: {target}")
                shutil.rmtree(target)
            except OSError as cleanup_error:
                cleanup_errors.append(str(cleanup_error))
        for parent in reversed(created_parents):
            try:
                parent.rmdir()
            except OSError as cleanup_error:
                # A directory that gained unrelated content must be preserved.
                if cleanup_error.errno not in (errno.ENOTEMPTY, errno.EEXIST):
                    cleanup_errors.append(str(cleanup_error))
        if cleanup_errors:
            raise OSError(f"{exc}; rollback incomplete: {'; '.join(cleanup_errors)}") from exc
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--agent", choices=ROOTS, action="append", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        targets = destinations(args.project, args.agent)
        if args.dry_run:
            print(json.dumps({"source": str(SOURCE), "destinations": [{"agent": a, "path": str(p)} for a, p in targets]}, indent=2))
        else:
            install_targets(args.project, targets)
            for agent, target in targets:
                print(f"Installed {agent} skill: {target}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"Cannot install skill: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
