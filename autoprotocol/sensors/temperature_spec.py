from sensors import TemperatureIR, TemperatureProbe

well_therm = TemperatureIR(pins={
    ...                 # TODO: Add pins later after picking, purchasing and figuring out interfacing for a component
})

# move_to_desired_well()
well_temp = well_therm.get()

plate.hold_temp(37)
    # Every x seconds, or every time you stop the shaker to do something:
        # Take a temperature reading with the IR sensor
        # Feed into PID round
        # Make change in output as per PID
