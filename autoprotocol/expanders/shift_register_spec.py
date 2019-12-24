from expanders import Shift_Register

shift_register_1 = Shift_Register(pins={
    'data': 2,
    'clock': 3,
    'latch': 4,
    'clear': 5,
    'output_enable': 6
}, virtual_pins=list(range(40, 55+1)))           # 16 pins for two chained shift registers, range is end-exclusive

# Raise some sort of error if:
# a) Real pins are in use
# b) Virtual pin numbers exist already as either real or virtual pins
# c) Some component is already using those virtual pins
# d) Pin is used as input
