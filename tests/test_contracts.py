import copy
import importlib.util
import json
import tempfile
import unittest
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


if __name__ == "__main__":
    unittest.main()
