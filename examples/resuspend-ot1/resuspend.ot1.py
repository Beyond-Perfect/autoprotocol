from opentrons import containers, instruments, robot

# a 12 row trough for sources
trough = containers.load('trough-12row', 'D2')


class Tubes:
    def __init__(self, *, pipette):
        self.pipette = pipette


# plate to create dinosaur in
# plate = containers.load('96-PCR-flat', 'C1')
tubes = {
    'A1': {'X': _, 'Y': _, 'Z': _},
    'A2': {'X': _, 'Y': _, 'Z': _},
    'A3': {'X': _, 'Y': _, 'Z': _},
    'A4': {'X': _, 'Y': _, 'Z': _},
    'A5': {'X': _, 'Y': _, 'Z': _},
    'A6': {'X': _, 'Y': _, 'Z': _},
    'A7': {'X': _, 'Y': _, 'Z': _},
    'A8': {'X': _, 'Y': _, 'Z': _},
    'B1': {'X': _, 'Y': _, 'Z': _},
    'B2': {'X': _, 'Y': _, 'Z': _},
    'B3': {'X': _, 'Y': _, 'Z': _},
    'B4': {'X': _, 'Y': _, 'Z': _},
    'B5': {'X': _, 'Y': _, 'Z': _},
    'B6': {'X': _, 'Y': _, 'Z': _},
    'B7': {'X': _, 'Y': _, 'Z': _},
    'B8': {'X': _, 'Y': _, 'Z': _},
    'C1': {'X': _, 'Y': _, 'Z': _},
    'C2': {'X': _, 'Y': _, 'Z': _},
    'C3': {'X': _, 'Y': _, 'Z': _},
    'C4': {'X': _, 'Y': _, 'Z': _},
    'C5': {'X': _, 'Y': _, 'Z': _},
    'C6': {'X': _, 'Y': _, 'Z': _},
    'C7': {'X': _, 'Y': _, 'Z': _},
    'C8': {'X': _, 'Y': _, 'Z': _},
}


def gen_move_to_tube(pipette):
    def move_to_tube(tube_name):
        pipette.move_to((robot._deck, tubes[tube_name]))

    return move_to_tube


# a tip rack for our pipette
p200rack = containers.load('tiprack-200ul', 'B2')

# wells to dispense dinosaur body in green
green_wells = [
    well.bottom() for well in plate.wells(
        'E1', 'D2', 'E2', 'D3', 'E3', 'F3', 'G3', 'H3',
        'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'C5', 'D5',
        'E5', 'F5', 'G5', 'C6', 'D6', 'E6', 'F6', 'G6',
        'C7', 'D7', 'E7', 'F7', 'G7', 'D8', 'E8', 'F8',
        'G8', 'H8', 'E9', 'F9', 'G9', 'H9', 'F10', 'G11',
        'H12')]

# wells to dispense dinosaur back plates in blue
blue_wells = [
    well.bottom() for well in plate.wells(
        'C3', 'B4', 'A5', 'B5', 'B6', 'A7', 'B7',
        'C8', 'C9', 'D9', 'E10', 'E11', 'F11', 'G12')]

# green solution location
green = trough.wells('A1')
# blue solution location
blue = trough.wells('A2')


def run_custom_protocol(pipette_axis: 'StringSelection...' = 'B (left side)'):
    p200 = instruments.Pipette(
        axis='b' if pipette_axis[0] == 'B' else 'a',
        min_volume=20,
        max_volume=200,
        tip_racks=[p200rack],
    )

    move_to_tube = gen_move_to_tube(p200)

    # macro commands like .distribute() make writing long sequences easier:
    # distribute green solution to the body
    p200.distribute(50, green, green_wells, disposal_vol=0, blow_out=True)
    # distribute blue solution to the dinosaur's back
    p200.distribute(50, blue, blue_wells, disposal_vol=0, blow_out=True)


run_custom_protocol(**{'pipette_axis': 'B (left side)'})
