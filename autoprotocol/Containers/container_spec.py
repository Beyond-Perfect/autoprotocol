from Containers import container

'''
The challenge I forsee with making all this stuff container focused, is that we are going to 
have to basically transcribing all the functionality of the opentrons API into a container 
focused API, because if you take your sensor suite readings though this container focused
style then it will be confusing and convoluted to use the built in opentrons functionality 
because its all 'instrument' focused.

Either way I do think being container focused style allows for an easier higher level interface 
and forces some level of orginization on the code, but it also is a lot more code to write rather 
than just making the a few sensor classes within the existing opentrons 'instrument' focused framework.
We have to build the underlying container/ probably placeable classes and a host of other shit.

Its very possible and we'll end with something probably better, but it seems like a good amount more work.
I'm just trying to make sure we aren't over engineering and missing a way that is simpler.
'''


sflask = Container(shake_flask('25ml'), 'position_1') # creates 25ml shake flask at position1 on deck

sflask.state()        # read out state of container, ie: empty, full, being probed...

sflask.pipette(5)     # pipettes 5 microliters into container

sflask.rd_temp()      # takes a temperature of container
#...
sflask.moved('position2') # tells robot that the container was moved to a different position without its knowledge




new_96 = Container(well_plate('96_brandname'), 'position_3') # creates 96 well plate in position 3 on deck

new_96.pipette(3, well=6) # pipettes 3 microliters into 6th well of container



