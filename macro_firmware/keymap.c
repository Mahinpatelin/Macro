#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_1, KC_2, KC_3, KC_4, KC_5,
        KC_6, KC_7, KC_8, KC_9, KC_MUTE
    )
};

// Controls what the Rotary Encoder does when turned
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_VOLU); // Volume Up
        } else {
            tap_code(KC_VOLD); // Volume Down
        }
    }
    return false;
}

// Controls what prints to the OLED screen
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_P(PSTR("Macro Pad Ready!\n"), false);
    return false;
}
#endif
