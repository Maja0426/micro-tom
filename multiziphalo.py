"""                     -micro:bit ZIP_Halo-
    4 különböző effekt használata, továbblépés mindig az "A" gombbal.
        A 3. effektnél "B" gombbal a neopixel színét változtatja.
      A 4. effektnél "A" gomb háttér színe, "B gomb pixelsor színe."

                            Használd bátran!"""
# written by Tamas Majoros

from microbit import *
from random import choice
import neopixel

# setup
np = neopixel.NeoPixel(pin0, 24)
red = [32, 0, 0]
green = [0, 32, 0]
blue = [0, 0, 32]
white = [32, 32, 32]
yellow = [32, 32, 0]
purple = [32, 0, 32]
cyan = [0, 32, 32]
color_block = [red, green, blue, white, yellow, purple, cyan]
color_b, color_f = 0, 3
num = 0

display.show('1')
sleep(1000)
display.clear()
np.clear()

# loop
while True:
    for neo_pix in range(0, 24, 2):
        np[neo_pix] = choice(color_block)
    for neo_pix in range(1, 24, 2):
        np[neo_pix] = choice(color_block)
    sleep(150)
    np.show()

    if button_a.was_pressed():
        break

display.show('2')
sleep(1000)
display.clear()
np.clear()

while True:
    for neo_pix in range(0, 24, 2):
        np[neo_pix] = red
        np.show()
        sleep(50)
    for neo_pix in range(1, 24, 2):
        np[neo_pix] = color_block[num]
        np.show()
        sleep(50)
    for neo_pix in range(0, 24, 2):
        np[neo_pix] = color_block[num]
        np.show()
        sleep(50)

    num +=1
    if num > 6:
        num = 0

    if button_a.was_pressed():
        break

display.show('3')
sleep(1000)
display.clear()
np.clear()
num = 0

while True:
    for neo_pix in range(0, 24):
        np[neo_pix] = color_block[num]
        np.show()
        sleep(50)
        np.clear()

    if button_b.was_pressed():
        num +=1
        if num > 6:
            num = 0

    if button_a.was_pressed():
        break

display.show('4')
sleep(1000)
display.clear()
np.clear()

while True:
    for a in range(0, 24, 4):
        for neo_pix in range(0, 24):
            np[neo_pix] = color_block[color_b]
            np.show()
        for neo_pix in range(a, a+4):
            np[neo_pix] = color_block[color_f]
            np.show()
        sleep(100)

        if a+8 > 24:
            a = 0

    if button_a.was_pressed():
            color_b +=1
            if color_b > 6:
                color_b = 0
    if button_b.was_pressed():
            color_f +=1
            if color_f > 6:
                color_f = 0
