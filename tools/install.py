#!/usr/bin/env python3
"""Copy the portable skill into explicit project-local agent directories."""

import argparse
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
            for agent, target in targets:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(SOURCE, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                print(f"Installed {agent} skill: {target}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"Cannot install skill: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
