import allthethings
import

NUM_SAMPLES_PER = 2

# Declare positions of everything and get objects for everything
sample_flasks = [
    Sample_Flask(some_position_data),
    Sample_Flask(some_other_position_data)
]
freeze_rack = Freeze_Rack(some_more_position_data)

# Take samples
for flask in sample_flasks:
    for _ in range(NUM_SAMPLES_PER):
        sample_flasks.sample(destination=freeze_rack)