#!/usr/bin/env python3
"""Cross-check the populated PCB controls against the QMK layout."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def main() -> int:
    pcb = (ROOT / "PCB" / "Macro Pad.kicad_pcb").read_text(encoding="utf-8")
    info = json.loads((ROOT / "macro_firmware" / "info.json").read_text(encoding="utf-8"))
    keymap = (ROOT / "macro_firmware" / "keymap.c").read_text(encoding="utf-8")

    cherry = count(r'\(property "Reference" "SW(?:[2-9])"', pcb)
    encoders = count(r'\(property "Value" "RotaryEncoder_Switch"', pcb)
    diodes = count(r'\(property "Reference" "D\d+"', pcb)
    layout = info["layouts"]["LAYOUT"]["layout"]
    matrix_positions = {tuple(item["matrix"]) for item in layout}

    layout_match = re.search(r"\[0\]\s*=\s*LAYOUT\((.*?)\)\s*\}\s*;", keymap, re.DOTALL)
    if not layout_match:
        raise SystemExit("FAIL: default LAYOUT call not found")
    firmware_keys = [x.strip() for x in layout_match.group(1).split(",") if x.strip()]

    checks = {
        "8 Cherry MX switch footprints": cherry == 8,
        "1 rotary encoder with push switch": encoders == 1,
        "9 isolation diodes": diodes == 9,
        "2 matrix rows": len(info["matrix_pins"]["rows"]) == 2,
        "5 matrix columns": len(info["matrix_pins"]["cols"]) == 5,
        "9 populated layout positions": len(matrix_positions) == 9,
        "row 1 / column 4 intentionally absent": (1, 4) not in matrix_positions,
        "firmware key count matches layout": len(firmware_keys) == len(layout),
    }

    for label, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}  {label}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
