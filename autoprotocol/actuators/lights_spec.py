from actuators import Lights

lights = Lights({
    'red1': 2,
    'green1': 3,
    'blue1': 4,
    'red2': 5,
    'green2': 6,
    'blue2': 7,
    'red3': 8,
    'green3': 9,
    'blue3': 10,
})

lights.on()					# Turn all lights on strip on

lights.on(0.5)				# Turn all lights on strip to 50%

lights.off()				# Turn all lights on strip off

lights.rgb(255, 0, 0)       # Set all lights to red

lights.segmentOn(1)         # Set segment 1 of 3 to on

lights.segmentOn(1, 0.5)    # Set segment 1 of 3 to on

lights.segmentOff(3)        # Set segment 3 of 3 to off

lights.segmentRGB(1, (255, 0, 0))   # Set segment 1 of 3 to red
