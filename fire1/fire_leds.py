# fire_leds.py -- simple LED fire simulation for CircuitPython
# 10 Oct 2022 - @todbot / Tod Kurt
# part of https://github.com/todbot/circuitpython_led_effects
#
# Note: requires boards with ulab (Numpy for CircuitPython) support

import time, random
from ulab import numpy as np

# a little class to help us do a fire simulation
class FireLEDs:
    def __init__(self,leds, fade_by, update_rate=0.01, fire_rate=0.1):
        self.leds = leds
        self.n = len(leds)
        self.leds_np = np.array( leds, dtype=np.int16)  # gets length from 'leds'
        self.fade_by = np.array( fade_by, dtype=np.int16 )
        self.last_time = time.monotonic()
        self.update_rate = update_rate
        self.last_fire_time = self.last_time
        self.fire_rate = fire_rate

    # call "update()" as fast as you want
    def update(self, new_color, update_num=3):
        now = time.monotonic()
        if now - self.last_time < self.update_rate:
            return
        self.last_time = now
        # using numpy, this global fade takes 4 msec for 256 LEDs on RP2040, otherwise takes 40 msec
        self.leds_np += self.fade_by  # fade down the working numpy array
        self.leds_np = np.clip(self.leds_np, 0,255)  # constrain all elements to 0-255
        if now - self.last_fire_time > self.fire_rate:
            self.last_fire_time = now + random.uniform(-self.fire_rate, self.fire_rate)
            c = (new_color>>16 & 0xff, new_color>>8 & 0xff, new_color & 0xff)  # turn color into list
            for i in range(update_num):
                self.leds_np[ random.randint(0,self.n-1) ] = c  # update random LEDs with new color
        self.leds[:] = self.leds_np.tolist()  # copy working numpy array to leds

    # call 'show()' whenever you want to update the actual LEDs
    def show(self):
        self.leds.show()
