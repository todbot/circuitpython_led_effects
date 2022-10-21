# fire_no_ulab.py  -- simple Neopixel fire animation using Python lists
# 10 Oct 2022 - @todbot / Tod Kurt
# part of https://github.com/todbot/circuitpython_led_effects

import time, random
import board, neopixel

num_leds = 256  # 256 even though we're only showing 64
led_pin = board.GP28

leds = neopixel.NeoPixel(led_pin, num_leds, brightness=0.4, auto_write=False)

fade_by = -3

fire_color = 0xff6600

while True:
    # pick a new random set of LEDs to light up with fire
    c = fire_color
    c = (c>>16 & 0xff, c>>8 & 0xff, c & 0xff)  # turn into tuple
    for i in range(3):
        leds[ random.randint(0,num_leds-1) ] = c

    start_time = time.monotonic()

    # fade down all LEDs, using Python lists, takes ~40 msec for 256 LEDs on RP2040
    leds[:] = [[min(max(i+fade_by,0),255) for i in l] for l in leds] # dim all by fade_by

    elapsed_time = time.monotonic() - start_time
    print(int(elapsed_time*1000))  # print out how long calculation took

    # update the strip
    leds.show()
