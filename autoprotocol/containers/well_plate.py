from containers import WellPlate, consts, Trough, Source, positions as pos

'''
Static:
- type of container
    - action of container
    - active area

Dynamic
- location

Sub
- sub-container
'''

plate = WellPlate(consts.plate96, pos.b3) # creates 25ml shake flask at position1 on deck
#or
plate = WellPlate('96well', 'b3')

water_source_1 = Trough(consts.rows12, pos.a1)
water_source_2 = Trough(consts.row12, pos.a2)

water = Source(water_source_1, water_source_2)

water_source_1.moved(pos.a3)

plate.well('a3').fill(water, 5)

plate.state()        # read out state of container, ie: empty, full, being probed...

plate.pipette(5)     # pipettes 5 microliters into container

plate.temp()      # takes a temperature of container
#...
plate.moved('position2') # tells robot that the container was moved to a different position without its knowledge




# new_96 = Container(well_plate('96_brandname'), 'position_3') # creates 96 well plate in position 3 on deck
#
# new_96.pipette(3, well=6) # pipettes 3 microliters into 6th well of container



