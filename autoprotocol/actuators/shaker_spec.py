from actuators import Shaker

shaker1 = Shaker(pins={
    'pot_out': 23           # Analog output simulating signal from potentiometer voltage divider to shaker input
})

shaker1.speed(rpm=3600)

shaker1.stop()
