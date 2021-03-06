from containers import container, consts


sflask = Container(shake_flask(consts.ML25), DECK_POSITIONS[1]) # creates 25ml shake flask at position1 on deck
#or 
sflask = Container(shake_flask('25ml'), DECK_POSITIONS[1]) 

sflask.state()        # read out state of container, ie: empty, full, being probed...

sflask.pipette(5)     # pipettes 5 microliters into container

sflask.rd_temp()      # takes a temperature of container
#...
sflask.moved('position2') # tells robot that the container was moved to a different position without its knowledge




new_96 = Container(well_plate('96_brandname'), 'position_3') # creates 96 well plate in position 3 on deck

new_96.pipette(3, well=6) # pipettes 3 microliters into 6th well of container



