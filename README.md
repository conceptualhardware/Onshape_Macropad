# Onshape_Macropad
Code for the onshape macropad.

This is a macropad built using the Pimoroni Keybow and the KPrepublic Enclosure.  

Assembly steps are as follows:
0. Order parts and wait
1. Install keyswitches into support bracket
2. Place kebow main board behind keyswitches
3. Press board into keyswitches until seated.
4. Place bracket into enclosure and screw in screws
5. Place back on enclosure and screw in screws
6. Connect to computer and copy over provided code to code.py
7. Save, then unplug and replug in macropad
8. Start up Onshape and work on designs.

Initial Layout w/ default code from Pimoroni
(as viewed looking straight at it)

3   7   b   f
2   6   a   e
1   5   9   d
0   4   8   c

Intended macro codes

e  , h  , v , i
S+F, c  , g , l
C+C, C+V, d , s+e
S+5, S+1, SB, ESC

C+ = Ctrl
S+ = Shift
SB = spacebar
Esc = escape

Colors
(by row)

Green
Red
Yellow
Blue

The colors are shown only when the key is pressed.

This makes use of the Adafruit HID Keyboard codes.

