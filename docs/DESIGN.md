# Engineering design record

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| R1 | Provide eight independently programmable mechanical keys | PCB footprint audit and hardware key test |
| R2 | Provide a rotary input for volume adjustment | Encoder direction test |
| R3 | Use encoder press as mute | QMK keymap inspection and hardware test |
| R4 | Support a small I²C status display | Schematic inspection and display bring-up |
| R5 | Connect over USB using an RP2040 controller | Enumeration and key-report test |
| R6 | Fit inside a printable enclosure | CAD interference check and trial assembly |
| R7 | Be reproducible from repository artifacts | Fresh-clone build and manufacturing-file review |

## Architecture

The XIAO RP2040 scans a two-row, five-column matrix. Eight Cherry MX switches occupy columns 0–3 across both rows. The encoder push switch occupies row 0, column 4; row 1, column 4 is intentionally empty. Each button path includes a diode and the firmware declares `COL2ROW` direction.

The encoder quadrature channels connect separately to GPIO pins GP2 and GP1. The OLED connector uses I²C on GP6/GP7. USB supplies power and carries HID reports.

## Key decisions

### Matrix instead of direct GPIO

A matrix reduces the GPIO count and reflects standard keyboard practice. With per-key diodes, simultaneous presses can be distinguished without phantom keys.

### XIAO RP2040

The compact module provides native USB, sufficient GPIO, QMK support, and an accessible UF2 bootloader while avoiding the risk of designing the high-speed USB and MCU support circuitry directly onto the first PCB revision.

### Through-hole switches and diodes

Through-hole parts simplify hand assembly and rework. The tradeoff is a larger board and more manual soldering than a surface-mount production design.

### Firmware-to-PCB consistency audit

Hardware and firmware can fail silently when a matrix position exists in software but is not populated in hardware. `tools/design_audit.py` makes this interface explicit and is suitable for CI.

## Engineering follow-ups

- Add dimensioned enclosure drawings and tolerance callouts after measuring a printed prototype.
- Record current consumption with and without the OLED.
- Capture electrical-rule and design-rule check reports from the exact KiCad version used for release.
- Add ESD protection and a reset/boot access strategy if the design is revised for repeated field use.
- Replace placeholder USB VID/PID values before any commercial distribution.
