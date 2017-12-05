""" micro:bit ZIP_Halo """
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
np.clear()

# loop

while True:
    for neo_pix in range(0, 24, 2):
        np[neo_pix] = choice(color_block)
    for neo_pix in range(1, 24, 2):
        np[neo_pix] = choice(color_block)
    sleep(150)
    np.show()
