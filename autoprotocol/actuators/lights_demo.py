from EmulatorGUI import GPIO
import threading
import time

DATA_PIN = 1
LATCH_PIN = 2
PUSH_OUT_PIN = 3
LED_COLORS = ["red", "green", "blue"]
LED_NUM_SEGS = 3

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PUSH_OUT_PIN, GPIO.OUT, initial=GPIO.LOW)

class Lights():
    SLEEP_DELAY = 0.000001                  # How long to wait between loops in the manual software PWM below
    TRIGGER_DELAY = 0.00000001              # How long to wait for digital signal propagation within the hardware
    PWM_TIMESLOTS = 100

    def __init__(self):
        # State of the three segments, first to third in order
        self.state = []
        for seg in range(LED_NUM_SEGS):
            self.state.append({})
            for color in LED_COLORS:
                self.state[seg][color] = 0.0

        self.thread = threading.Thread(target=self._thread_func, args=())

    def _thread_func(self):
        current_time_ratio = 0.0                 # How far into the timeslots we currently are, from 0 to 1
        time_ratio_advance = 1.0 / self.PWM_TIMESLOTS

        while time.sleep(self.SLEEP_DELAY):
            # Set LEDs to appropriate values
            for seg in range(LED_NUM_SEGS):
                for color in LED_COLORS:
                    # IMPORTANT: Implicitly dictates pin order for LEDs after shift register below
                    if self.state[seg][color] > current_time_ratio:
                        # Push a high on the shift register
                        GPIO.output(DATA_PIN, GPIO.high)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(LATCH_PIN, GPIO.high)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(LATCH_PIN, GPIO.low)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(DATA_PIN, GPIO.low)
                    else:
                        # Push a low on the shift register
                        GPIO.output(DATA_PIN, GPIO.low)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(LATCH_PIN, GPIO.high)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(LATCH_PIN, GPIO.low)
                        time.sleep(self.TRIGGER_DELAY)
                        GPIO.output(DATA_PIN, GPIO.low)

            # Push updated states out to LED strip
            time.sleep(self.TRIGGER_DELAY)
            GPIO.output(PUSH_OUT_PIN, GPIO.high)
            time.sleep(self.TRIGGER_DELAY)
            GPIO.output(PUSH_OUT_PIN, GPIO.low)

            # Increment segment, resetting upon reaching 1 to 0
            current_time_ratio += time_ratio_advance
            if current_time_ratio == 1.0:
                current_time_ratio = 0.0

    def on(self):					                    # Turn all lights on strip on
        for seg in range(LED_NUM_SEGS):
            for color in LED_COLORS:
                self.state[seg][color] = 1.0

    def off(self):				                        # Turn all lights on strip off
        for seg in range(LED_NUM_SEGS):
            for color in LED_COLORS:
                self.state[seg][color] = 0.0

    def rgb(self, *colors):                             # Set all lights to a given color
        for seg in range(LED_NUM_SEGS):
            for color_index, color in enumerate(LED_COLORS):
                self.state[seg][color] = colors[color_index]

    def segmentOn(self, segment_num, brightness=1.0):   # Turn a single segment on to an optional given brightness
        for color in LED_COLORS:
            self.state[segment_num][color] = brightness

    def segmentOff(self, segment_num):                  # Turn a single segment off
        for color in LED_COLORS:
            self.state[segment_num][color] = 0.0

    def segmentRGB(self, segment_num, *colors):         # Set a single segment to a given color
        for color_index, color in enumerate(LED_COLORS):
            self.state[segment_num][color] = colors[color_index]
