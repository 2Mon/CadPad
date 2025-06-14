import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryEncoder
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.oled import OLED

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = RotaryEncoder(
    pins=(board.D7, board.D9),
    resolution=4,
    pos_side=(KC.LCTL, KC.EQUAL),  #Ctrl + = zoom in
    neg_side=(KC.LCTL, KC.MINS)    #Ctrl + - zoom out
)
layers = Layers()
keyboard.modules.append(layers)

oled = OLED(pin_scl=board.SCL, pin_sda=board.SDA, width=128, height=32)
keyboard.modules.append(oled)

keyboard.keymap = [
    [
        (KC.LSFT, KC.E),  #New Sketch
        (KC.LSFT, KC.F),  #Fillet
        (KC.LSFT, KC.C),  #Chamfer
    ],
    [
        (KC.LSFT, KC.X),  #Extrude
        (KC.LSFT, KC.O),  #Offset
        (KC.LSFT, KC.R),  #Revolve
    ],
    [
        (KC.LSFT, KC.M),  #Mirror
        (KC.LSFT, KC.T),  #Trim
        (KC.LSFT, KC.P),  #Pattern
    ]
]

if __name__ == '__main__':
    keyboard.go()
