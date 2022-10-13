# code.py for fire1 -- demonstrate using the "fire_leds" library
# 10 Oct 2022 - @todbot / Tod Kurt
# Drop this code.py and fire_leds.py into your CIRCUITPY drive
# part of https://github.com/todbot/circuitpython_led_effects

import time, board, neopixel, rainbowio

import fire_leds

fire_color = 0xff5500
fire_fade = (-2,-2,-2)  # how much to fade R,G,B each udpate

num_leds = 64 * 1
led_pin = board.GP28

leds = neopixel.NeoPixel(led_pin, num_leds, brightness=0.4, auto_write=False)

# make up our fire
#fire_leds = fire_leds.FireLEDs(leds, fade_by=fire_fade, fire_rate=0.1 )
fire_leds = fire_leds.FireLEDs(leds, fade_by=fire_fade)

while True:
    #fire_leds.update( rainbowio.colorwheel(time.monotonic()*40), 3 )  # rainbow fire
    fire_leds.update( fire_color, 3 )  # standard fire effect
    fire_leds.show()
