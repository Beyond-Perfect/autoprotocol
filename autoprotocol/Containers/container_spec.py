from Containers import container, deck, sflask, well_plate
import actuators *  
import sensors *                        
'''
not sure whether it makes more sense for operator to import
the actuators/sensors they are going to use or just the whole suite of them
it just seems simpler if they import all the actuators/sensors and then import 
'''

new_deck = Container(deck())

new_deck.webcam(on)                     #turn webcam on

new_deck.webcam(off)                    #turn webcam off

new_deck.webcam(record(start))          #has the webcam start recording

new_deck.webcam(record(stop))           #has the webcam stop recording

new_deck.webcam(record(30))             #has webcam start recording for 30 minutes

new_deck.webcam(record(30), post=True)  #has the webcam start recording for 30 minutes and then push to server

new_deck.lights(on)                     #turns LEDs on in the robot

new_deck.lights(off)                    #turns LEDs off in the robot

new_deck.lights(rgb(255, 0, 0))         #allows operator to define color of the lights

new_deck.lights(red)                    #turns LEDs red

new_deck.lights(green)                  #turns LEDs green

new_deck.lights(blue)                   #turns LEDs blue

new_deck.lights(white)                  #turns LEDs white





sflask = Container(shake_flask('25ml'), 'position_1') # creates 25ml shake flask at position1 on deck

sflask.state()        # read out state of container, ie: empty, full, being probed...

sflask.pipette(5)     # pipettes 5 microliters into container

sflask.rd_temp()      # takes a temperature of container

sflask.shake(shaker=enable) #loads shaker onto deck

sflask.shake(2.5, 100)  #shakes shake flask for 2.5 minutes at 100rpm
#...
sflask.moved('position2') # tells robot that the container was moved to a different position without its knowledge



new_96 = Container(well_plate('96_brandname'), 'position_3') # creates 96 well plate in position 3 on deck

new_96.pipette(3, well=6) # pipettes 3 microliters into 6th well of container



