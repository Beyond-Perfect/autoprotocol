import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                   # calling for time to provide delays in program
from autoprotocol._component import Component

# Credits to:
# https://circuitdigest.com/microcontroller-projects/raspberry-pi-74hc595-shift-register-tutorial


class Lights(Component):
    def __init__(self):
        super(Lights, self).__init__(is_pin_not_pins=False, pin_names=['clock_pin, data_pin, output_buffer_pin'])
        self._lights = {}

        IO.setmode(IO.BOARD)                         # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)


    def register(self, *, pins=None, name):
        self._lights['name'] = {
            'clock_pin': pins['clock_pin'],
            'data_pin': pins['data_pin'],
            'output_buffer_pin': pins['output_buffer_pin']
        }

        # Initialize relevant GPIO pins as outputs
        IO.setup(self._lights['clock_pin'], IO.OUT)
        IO.setup(self._lights['data_pin'], IO.OUT)
        IO.setup(self._lights['output_buffer_pin'], IO.OUT)

    def enable(self, name):



while 1:                               # execute loop forever
    for y in range(8):            # loop for counting up 8 times
        IO.output(4,1)            # pull up the data pin for every bit.
        time.sleep(0.01)            # wait for 100ms
        IO.output(5,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(5,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(4,0)            # clear the DATA pin
        IO.output(6,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(6,0)            # pull down the SHIFT pin

    for y in range(8):            # loop for counting up 8 times
        IO.output(4,0)            # clear the DATA pin, to send 0
        time.sleep(0.1)            # wait for 100ms
        IO.output(5,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(5,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(4,0)            # keep the DATA bit low to keep the countdown
        IO.output(6,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(6,0)