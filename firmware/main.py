import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D4, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=True,
)

keyboard.keymap = [
    [KC.CTRL, KC.C, KC.V]
]

if __name__ == '__main__':
    keyboard.go()