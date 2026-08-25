# Build and bring-up guide

## 1. Review before ordering

1. Open the schematic and PCB in KiCad.
2. Run electrical-rule checking and design-rule checking.
3. Inspect switch orientation, diode polarity, XIAO orientation, OLED header order, board outline, holes, and copper clearances.
4. Compare the generated Gerbers with the editable PCB. Re-generate them if sources changed.

## 2. Suggested assembly order

1. Diodes, observing polarity.
2. Low-profile headers and connectors.
3. XIAO sockets or module headers.
4. Mechanical switches and encoder.
5. OLED header; attach the OLED only after rail checks.

Inspect every solder joint and remove flux residue as appropriate. Do not connect USB yet.

## 3. Electrical checks

- Confirm there is no short between power and ground.
- Confirm each diode conducts in one direction only.
- Confirm each switch closes the intended row/column path.
- Verify the OLED header pin order against the selected display module.

## 4. Firmware

Copy `macro_firmware` into a QMK keyboard directory and compile its default keymap. Flash the UF2 using the RP2040 bootloader. The default map is:

```text
Top electrical row:    1  2  3  4  Mute (encoder press)
Bottom electrical row: 5  6  7  8
Encoder rotation:      Volume down / volume up
```

## 5. Functional test

| Test | Expected result |
|---|---|
| USB enumeration | Host recognizes a keyboard |
| Eight switches | Keys 1–8 register once per press |
| Encoder clockwise | Volume increases |
| Encoder counterclockwise | Volume decreases |
| Encoder press | Mute toggles |
| OLED fitted | Status text appears without bus errors |

Record anomalies in an issue before changing both hardware and firmware at the same time.

## 6. Mechanical assembly

Slice `CAD/case.stl` using material-appropriate settings. Before a full print, verify the switch plate thickness, USB clearance, encoder height, and PCB mounting method. Use a first-article print to establish printer-specific fit compensation.
