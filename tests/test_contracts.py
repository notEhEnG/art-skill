import copy
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


planner = module_at("planner", ROOT / "skills/art-skill/scripts/plan_pack.py")
installer = module_at("installer", ROOT / "tools/install.py")


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.brief = json.loads((ROOT / "examples/rainy-reading-room.brief.json").read_text(encoding="utf-8"))

    def test_example_has_four_jobs_and_two_repairs_without_generation(self):
        plan = planner.build_plan(self.brief)
        self.assertEqual((plan["base_calls"], plan["repair_allowance"], plan["calls_used"]), (4, 2, 0))
        self.assertFalse(plan["generation_performed"])
        self.assertIsNone(plan["actual_cost_usd"])

    def test_every_recipe_can_plan_the_example(self):
        for recipe in sorted(planner.STYLE_ROOT.glob("*.json")):
            with self.subTest(style=recipe.stem):
                brief = copy.deepcopy(self.brief)
                brief["style"] = recipe.stem
                plan = planner.build_plan(brief)
                self.assertEqual(plan["style_lock"]["id"], recipe.stem)
                self.assertEqual(len(plan["style_lock"]["sha256"]), 64)

    def test_chain_of_derivatives_is_rejected(self):
        self.brief["assets"][2]["reference"] = "cover"
        with self.assertRaisesRegex(ValueError, "first asset directly"):
            planner.build_plan(self.brief)

    def test_budget_is_total_not_per_asset(self):
        for cap in [3, 13, True]:
            with self.subTest(cap=cap):
                self.brief["max_calls"] = cap
                with self.assertRaisesRegex(ValueError, "max_calls"):
                    planner.build_plan(self.brief)

    def test_transparent_jpeg_is_rejected(self):
        self.brief["assets"][-1]["format"] = "jpeg"
        with self.assertRaisesRegex(ValueError, "transparent assets"):
            planner.build_plan(self.brief)

    def test_duplicate_and_unsafe_asset_ids_are_rejected(self):
        for value in ["anchor", "../escape", "con"]:
            with self.subTest(value=value):
                self.brief["assets"][1]["id"] = value
                with self.assertRaises(ValueError):
                    planner.build_plan(self.brief)

    def test_unknown_style_is_rejected(self):
        self.brief["style"] = "unverified-magic-style"
        with self.assertRaisesRegex(ValueError, "unknown style"):
            planner.build_plan(self.brief)

    def test_planner_refuses_overwriting_a_reviewed_file(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "reviewed.json"
            out.write_text("keep", encoding="utf-8")
            result = planner.main([str(ROOT / "examples/rainy-reading-room.brief.json"), "--out", str(out)])
            self.assertEqual(result, 2)
            self.assertEqual(out.read_text(), "keep")

    def test_project_installations_include_resources_and_preserve_existing(self):
        with tempfile.TemporaryDirectory() as folder:
            result = installer.main(["--project", folder, "--agent", "codex", "--agent", "claude", "--agent", "cursor"])
            self.assertEqual(result, 0)
            for dirname in installer.ROOTS.values():
                target = Path(folder) / dirname / "skills/art-skill"
                self.assertTrue((target / "SKILL.md").is_file())
                self.assertEqual(
                    {path.name for path in (target / "assets/styles").glob("*.json")},
                    {path.name for path in planner.STYLE_ROOT.glob("*.json")},
                )
            self.assertEqual(installer.main(["--project", folder, "--agent", "codex"]), 2)

    def test_failed_copy_rolls_back_partial_and_completed_copies(self):
        for failed_agent in ("codex", "claude"):
            with self.subTest(failed_agent=failed_agent), tempfile.TemporaryDirectory() as folder:
                project = Path(folder).resolve()
                keep = project / ".claude/skills/existing-skill/keep.txt"
                keep.parent.mkdir(parents=True)
                keep.write_text("keep", encoding="utf-8")
                before = {p.relative_to(project) for p in project.rglob("*")}
                failed_target = project / installer.ROOTS[failed_agent] / "skills/art-skill"
                real_copytree = installer.shutil.copytree

                def fail_copy(source, destination, *args, **kwargs):
                    if Path(destination) == failed_target:
                        if failed_agent == "claude":
                            self.assertTrue((project / ".agents/skills/art-skill/SKILL.md").is_file())
                        (Path(destination) / "partial.txt").write_text("partial", encoding="utf-8")
                        raise OSError("simulated copy failure")
                    return real_copytree(source, destination, *args, **kwargs)

                stdout, stderr = io.StringIO(), io.StringIO()
                with mock.patch.object(installer.shutil, "copytree", side_effect=fail_copy), \
                     contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    result = installer.main(["--project", folder, "--agent", "codex", "--agent", "claude", "--agent", "cursor"])
                self.assertEqual(result, 2)
                self.assertIn("simulated copy failure", stderr.getvalue())
                self.assertNotIn("Installed", stdout.getvalue())
                self.assertEqual({p.relative_to(project) for p in project.rglob("*")}, before)
                self.assertEqual(keep.read_text(encoding="utf-8"), "keep")

    def test_target_created_after_preflight_is_preserved_during_rollback(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder).resolve()
            keep = project / ".claude/skills/art-skill/keep.txt"
            real_destinations = installer.destinations

            def create_later_target(*args):
                targets = real_destinations(*args)
                keep.parent.mkdir(parents=True)
                keep.write_text("another installation", encoding="utf-8")
                return targets

            with mock.patch.object(installer, "destinations", side_effect=create_later_target), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                result = installer.main(["--project", folder, "--agent", "codex", "--agent", "claude"])
            self.assertEqual(result, 2)
            self.assertEqual(keep.read_text(encoding="utf-8"), "another installation")
            self.assertFalse((project / ".agents").exists())

    def test_interrupted_copy_rolls_back_the_claimed_target(self):
        with tempfile.TemporaryDirectory() as folder:
            with mock.patch.object(installer.shutil, "copytree", side_effect=KeyboardInterrupt), \
                 self.assertRaises(KeyboardInterrupt):
                installer.main(["--project", folder, "--agent", "codex"])
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_dry_run_creates_no_installation_directories(self):
        with tempfile.TemporaryDirectory() as folder:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                result = installer.main(["--project", folder, "--agent", "codex", "--agent", "claude", "--dry-run"])
            self.assertEqual(result, 0)
            self.assertEqual(len(json.loads(stdout.getvalue())["destinations"]), 2)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_rollback_failure_reports_the_original_error_and_remaining_target(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / ".agents/skills/art-skill"
            stderr = io.StringIO()
            with mock.patch.object(installer.shutil, "copytree", side_effect=OSError("copy failed")), \
                 mock.patch.object(installer.shutil, "rmtree", side_effect=PermissionError(f"cannot remove {target}")), \
                 contextlib.redirect_stderr(stderr):
                result = installer.main(["--project", folder, "--agent", "codex"])
            self.assertEqual(result, 2)
            self.assertIn("copy failed", stderr.getvalue())
            self.assertIn("rollback incomplete", stderr.getvalue())
            self.assertIn(str(target), stderr.getvalue())
            self.assertTrue(target.is_dir())


if __name__ == "__main__":
    unittest.main()
