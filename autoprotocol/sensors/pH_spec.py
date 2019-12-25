from sensors import pH

#container first:
well_pH = pH(pins = {

...
} )

well_pH.take_rd()       #probe: takes pH reading of well, stores it, and then puts sensor in sterilization box
                        #sample: Takes small sample puts it on pH paper, pi Camera classifies reading and records classification
              
              
#instrument first:
pH_probe = pH(pins= {
...
})

pH_probe.clean()          # probe: puts probe in sterilizing box/solution
                          # sample: 
                          
pH_probe.clean_status()   # probe: reads out the clean status of the probe (unclean, cleaning/drying , clean)

pH_probe.take_rd()
pH_probe.take_rd(well_1)
pH_probe.take_rd(well_1, 15) #every 15 minutes








'''
There are two potential applications of this task,
either we use a pH probe and stick it in the solution 
get a reading and then santize it in alcohol and then
make sure the alcohol is dry by the next use or we 
sanatize it using a UV light in a separate box.

The other option is to have pH paper strips have the 
pipette take the minimum sample put it on the strips
and then have the camera go over to the strips and log
what the pH color reading is.

There could be other better implemetations but I haven't 
thought of any.
'''
