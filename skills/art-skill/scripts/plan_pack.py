#!/usr/bin/env python3
"""Validate a brief and emit a portable image plan. Makes no network calls."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SIZES = {"1024x1024", "1536x1024", "1024x1536"}
FORMATS = {"png", "jpeg", "webp"}
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
STYLE_ROOT = Path(__file__).resolve().parents[1] / "assets" / "styles"


def identifier(value, label):
    if not isinstance(value, str) or len(value) > 63 or not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", value):
        raise ValueError(f"{label} must be a lowercase hyphenated identifier")
    if value in RESERVED:
        raise ValueError(f"{label} is a reserved filename")
    return value


def text_field(value, label):
    if not isinstance(value, str) or not value.strip() or len(value) > 5000:
        raise ValueError(f"{label} must be nonempty text of at most 5000 characters")
    return value.strip()


def build_plan(brief):
    if not isinstance(brief, dict) or brief.get("schema_version") != "1.0":
        raise ValueError("brief schema_version must be 1.0")
    pack_id = identifier(brief.get("id"), "id")
    style_id = identifier(brief.get("style"), "style")
    style_path = STYLE_ROOT / f"{style_id}.json"
    if not style_path.is_file():
        raise ValueError(f"unknown style: {style_id}")
    style_bytes = style_path.read_bytes()
    recipe = json.loads(style_bytes)
    subject = text_field(brief.get("subject"), "subject")
    purpose = text_field(brief.get("purpose"), "purpose")
    constraints = brief.get("constraints", [])
    if not isinstance(constraints, list) or len(constraints) > 30:
        raise ValueError("constraints must be a list with at most 30 entries")
    constraints = [text_field(c, "constraint") for c in constraints]
    assets = brief.get("assets")
    if not isinstance(assets, list) or not 1 <= len(assets) <= 12:
        raise ValueError("assets must contain between 1 and 12 entries")
    cap = brief.get("max_calls")
    if type(cap) is not int or not len(assets) <= cap <= 12:
        raise ValueError("max_calls must be an integer from asset count to 12, including repairs")

    jobs, seen, anchor = [], set(), None
    traits = recipe["traits"]
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            raise ValueError("each asset must be an object")
        asset_id = identifier(asset.get("id"), "asset id")
        if asset_id in seen:
            raise ValueError(f"duplicate asset id: {asset_id}")
        seen.add(asset_id)
        role = text_field(asset.get("role"), "asset role")
        direction = text_field(asset.get("direction"), "asset direction")
        size, background, fmt = asset.get("size"), asset.get("background"), asset.get("format")
        if not isinstance(size, str) or size not in SIZES:
            raise ValueError("asset size must be 1024x1024, 1536x1024 or 1024x1536")
        if background not in ("opaque", "transparent"):
            raise ValueError("asset background must be opaque or transparent")
        if not isinstance(fmt, str) or fmt not in FORMATS:
            raise ValueError("asset format must be png, jpeg or webp")
        if background == "transparent" and fmt == "jpeg":
            raise ValueError("transparent assets require png or webp")
        if index == 0:
            if asset.get("reference") is not None:
                raise ValueError("first asset is the anchor and cannot have a reference")
            anchor, reference = asset_id, None
        else:
            reference = asset.get("reference")
            if reference != anchor:
                raise ValueError("every derivative must reference the first asset directly")
        lines = [
            "Use case: stylized-concept",
            f"Asset type: {role}; intended use: {purpose}",
            f"Primary request: {subject}",
            f"Style/medium: {traits['medium']}",
            f"Color palette: {', '.join(traits['palette'])}",
            f"Materials/textures: {traits['texture']}",
            f"Composition/framing: {traits['composition']}; {direction}",
            f"Lighting/mood: {traits['lighting']}",
            f"Requested output target: {size}, {background} background, {fmt}; use only supported tool controls",
            "Avoid: " + "; ".join(recipe["avoid"]),
        ]
        if reference:
            lines.append(f"Input images: accepted {anchor} artwork as shared reference; preserve applicable palette, materials and subject details")
        if constraints:
            lines.append("Constraints: " + "; ".join(constraints))
        extension = "jpg" if fmt == "jpeg" else fmt
        jobs.append({
            "id": asset_id, "role": role, "status": "planned", "reference": reference,
            "requested_size": size, "requested_background": background, "requested_format": fmt,
            "planned_path": f"images/{asset_id}.{extension}", "prompt": "\n".join(lines),
        })
    return {
        "schema_version": "1.0", "pack_id": pack_id, "status": "planned",
        "generation_performed": False, "backend": None, "model": None,
        "style_lock": {"id": style_id, "version": recipe["version"], "sha256": hashlib.sha256(style_bytes).hexdigest(), "recipe": recipe},
        "anchor_asset_id": anchor, "base_calls": len(jobs), "max_calls": cap,
        "repair_allowance": cap - len(jobs), "calls_used": 0, "actual_cost_usd": None,
        "assets": jobs,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path)
    parser.add_argument("--out", type=Path, help="New JSON file; existing files are never overwritten")
    args = parser.parse_args(argv)
    try:
        plan = build_plan(json.loads(args.brief.read_text(encoding="utf-8-sig")))
        payload = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with args.out.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(payload)
            print(f"Saved plan: {args.out.resolve()}")
        else:
            print(payload, end="")
        return 0
    except (OSError, ValueError) as exc:
        print(f"Cannot plan pack: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
