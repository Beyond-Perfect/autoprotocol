from ADC import Mcp3008

adc = Mcp3008(pins={
    'SCLK': 20,
    'DOUT': 21,         # MOSI in SPI standard
    'DIN':  22,         # MISO in SPI standard
    'CS':   23
}, virtual_pins=list(range(40, 47+1)))

# Could potentially use mcp3008.c (doesn't exist) in https://github.com/WiringPi/WiringPi/tree/master/wiringPi instead
