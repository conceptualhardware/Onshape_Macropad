# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# A simple example of how to set up a keymap and HID keyboard on Keybow 2040.

# You'll need to connect Keybow 2040 to a computer, as you would with a regular
# USB keyboard.

# Drop the keybow2040.py file into your `lib` folder on your `CIRCUITPY` drive.

# NOTE! Requires the adafruit_hid CircuitPython library also!

import board
from keybow2040 import Keybow2040

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# A map of keycodes that will be mapped sequentially to each of the keys, 0-15

keymap = [ #MODIFIER, KEY, COLOR
            [[Keycode.SHIFT, Keycode.FIVE], (0, 0, 255)], #0,0
            [[Keycode.CONTROL, Keycode.C], (255, 255, 0)], #1,0
            [[Keycode.SHIFT  , Keycode.F], (255, 0, 0)], #2,0
            [[Keycode.E], (0, 255, 0)], #3,0
            [[Keycode.SHIFT	, Keycode.ONE], (0, 0, 255)], #0,1
            [[Keycode.CONTROL, Keycode.V], (255, 255, 0)], #1,1
            [[Keycode.C], (255, 0, 0)], #2,1
            [[Keycode.H], (0, 255, 0)], #3,1
            [[Keycode.SPACEBAR], (0, 0, 255)],	#0,2		
            [[Keycode.D], (255, 255, 0)], #1,2
            [[Keycode.G], (255, 0, 0)], #2,2
            [[Keycode.V], (0, 255, 0)], #3,2
            [[Keycode.ESCAPE ],	(0, 0, 255)], #0,3
            [[Keycode.SHIFT, Keycode.E], (255, 255, 0)], #1,3
            [[Keycode.L], (255, 0, 0)], #2,3
            [[Keycode.I], (0, 255, 0)], #3,3]
]
# The colour to set the keys when pressed, yellow.
rgb = (255, 255, 0)

# Attach handler functions to all of the keys
for key in keys:
    # A press handler that sends the keycode and turns on the LED
    @keybow.on_press(key)
    def press_handler(key):
        keycode = keymap[key.number][0]
        print(keycode)
        key.set_led(*keymap[key.number][1])
        if len(keycode) == 2:
            keyboard.send(keycode[0],keycode[1])
        else: keyboard.send(keycode[0])
#keycode = keymap[key.number]
#keyboard.send(keycode)
#key.set_led(*rgb)

    # A release handler that turns off the LED
    @keybow.on_release(key)
    def release_handler(key):
        key.led_off()

while True:
    # Always remember to call keybow.update()!
    keybow.update()
