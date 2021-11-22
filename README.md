# Onshape_Macropad
Code for the onshape macropad.


![onshape_macropad](https://github.com/conceptualhardware/Onshape_Macropad/blob/main/onshape_macropad.jpg)


This is a macropad built using the Pimoroni Keybow and the KPrepublic Enclosure.  


![pimoroni_keybow](https://cdn.shopify.com/s/files/1/0174/1800/products/keybow-2040-2_large.jpg?v=1618327651)

[pimoroni_keybow](https://shop.pimoroni.com/products/keybow-2040?variant=39328275300435)


![kprepublic_enclosure](https://cdn.shopify.com/s/files/1/2711/4238/products/JJ4x4case-11.jpg?v=1617001143)

[kprepublic enclosure](https://kprepublic.com/products/anodized-aluminium-cubic-case-for-jj4x4-jj4-custom-keyboard-acrylic-panels-stalinite-diffuser-can-support-rotary-brace-supporter)


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

3
7
b
f

2
6
a
e

1
5
9
d

0
4
8
c


Intended macro codes

e,
h,
v,
i

S+F,
c,
g,
l

C+C,
C+V,
d,
s+e

S+5,
S+1,
SB,
ESC


Legend:

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

