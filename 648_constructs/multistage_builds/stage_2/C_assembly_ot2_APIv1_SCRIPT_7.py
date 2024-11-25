from opentrons import labware, instruments, modules, robot
import numpy as np


final_assembly_dict={"A1": [["E6", "A10", "H11"], [1, 2, 1]], "B1": [["E6", "A10", "A12"], [1, 2, 1]], "C1": [["E6", "A10", "B12"], [1, 2, 1]], "D1": [["E6", "A10", "C12"], [1, 2, 1]], "E1": [["E6", "A10", "D12"], [1, 2, 1]], "F1": [["E6", "A10", "E12"], [1, 2, 1]], "G1": [["E6", "A10", "F12"], [1, 2, 1]], "H1": [["E6", "A10", "G12"], [1, 2, 1]], "A2": [["E6", "A10", "H12"], [1, 2, 1]], "B2": [["F6", "B10", "H11"], [1, 2, 1]], "C2": [["F6", "B10", "A12"], [1, 2, 1]], "D2": [["F6", "B10", "B12"], [1, 2, 1]], "E2": [["F6", "B10", "C12"], [1, 2, 1]], "F2": [["F6", "B10", "D12"], [1, 2, 1]], "G2": [["F6", "B10", "E12"], [1, 2, 1]], "H2": [["F6", "B10", "F12"], [1, 2, 1]], "A3": [["F6", "B10", "G12"], [1, 2, 1]], "B3": [["F6", "B10", "H12"], [1, 2, 1]], "C3": [["F6", "C10", "D1"], [1, 2, 2]], "D3": [["F6", "C10", "E1"], [1, 2, 2]], "E3": [["F6", "C10", "F1"], [1, 2, 2]], "F3": [["F6", "C10", "G1"], [1, 2, 2]], "G3": [["G6", "C10", "H1"], [1, 2, 2]], "H3": [["G6", "C10", "A2"], [1, 2, 2]], "A4": [["G6", "C10", "B2"], [1, 2, 2]], "B4": [["G6", "C10", "C2"], [1, 2, 2]], "C4": [["G6", "C10", "D2"], [1, 2, 2]], "D4": [["G6", "D10", "D1"], [1, 2, 2]], "E4": [["G6", "D10", "E1"], [1, 2, 2]], "F4": [["G6", "D10", "F1"], [1, 2, 2]], "G4": [["G6", "D10", "G1"], [1, 2, 2]], "H4": [["G6", "D10", "H1"], [1, 2, 2]], "A5": [["G6", "D10", "A2"], [1, 2, 2]], "B5": [["G6", "D10", "B2"], [1, 2, 2]], "C5": [["G6", "D10", "C2"], [1, 2, 2]], "D5": [["H6", "D10", "D2"], [1, 2, 2]], "E5": [["H6", "E10", "D1"], [1, 2, 2]], "F5": [["H6", "E10", "E1"], [1, 2, 2]], "G5": [["H6", "E10", "F1"], [1, 2, 2]], "H5": [["H6", "E10", "G1"], [1, 2, 2]], "A6": [["H6", "E10", "H1"], [1, 2, 2]], "B6": [["H6", "E10", "A2"], [1, 2, 2]], "C6": [["H6", "E10", "B2"], [1, 2, 2]], "D6": [["H6", "E10", "C2"], [1, 2, 2]], "E6": [["H6", "E10", "D2"], [1, 2, 2]], "F6": [["H6", "F10", "H2"], [1, 2, 2]], "G6": [["H6", "F10", "A3"], [1, 2, 2]], "H6": [["H6", "F10", "B3"], [1, 2, 2]], "A7": [["A7", "F10", "C3"], [1, 2, 2]], "B7": [["A7", "F10", "D3"], [1, 2, 2]], "C7": [["A7", "F10", "E3"], [1, 2, 2]], "D7": [["A7", "F10", "F3"], [1, 2, 2]], "E7": [["A7", "F10", "G3"], [1, 2, 2]], "F7": [["A7", "F10", "H3"], [1, 2, 2]], "G7": [["A7", "G10", "H2"], [1, 2, 2]], "H7": [["A7", "G10", "A3"], [1, 2, 2]], "A8": [["A7", "G10", "B3"], [1, 2, 2]], "B8": [["A7", "G10", "C3"], [1, 2, 2]], "C8": [["A7", "G10", "D3"], [1, 2, 2]], "D8": [["A7", "G10", "E3"], [1, 2, 2]], "E8": [["A7", "G10", "F3"], [1, 2, 2]], "F8": [["B7", "G10", "G3"], [1, 2, 2]], "G8": [["B7", "G10", "H3"], [1, 2, 2]], "H8": [["B7", "H10", "H2"], [1, 2, 2]], "A9": [["B7", "H10", "A3"], [1, 2, 2]], "B9": [["B7", "H10", "B3"], [1, 2, 2]], "C9": [["B7", "H10", "C3"], [1, 2, 2]], "D9": [["B7", "H10", "D3"], [1, 2, 2]], "E9": [["B7", "H10", "E3"], [1, 2, 2]], "F9": [["B7", "H10", "F3"], [1, 2, 2]], "G9": [["B7", "H10", "G3"], [1, 2, 2]], "H9": [["B7", "H10", "H3"], [1, 2, 2]]}
tiprack_num=3


def final_assembly(final_assembly_dict, tiprack_num, tiprack_type="tiprack-10ul"):
    """Implements final assembly reactions using an opentrons OT-2.

    Args:
    final_assembly_dict (dict): Dictionary with keys and values corresponding to destination and associated linker-ligated part wells, respectively.
    tiprack_num (int): Number of tipracks required during run.

    """

    # Constants
    CANDIDATE_TIPRACK_SLOTS = ['3', '6', '9', '2', '5', '8', '11']
    PIPETTE_MOUNT = 'right'
    MAG_PLATE_TYPE = '4ti-0960_FrameStar'
    MAG_PLATE_POSITION = '1'
    TUBE_RACK_TYPE = 'tube-rack_E1415-1500'
    TUBE_RACK_POSITION = '7'
    DESTINATION_PLATE_TYPE = 'aluminium-block_4ti-0960_FrameStar'
    TEMPDECK_SLOT = '4'
    TEMP = 20
    TOTAL_VOL = 15
    PART_VOL = 1.5
    MIX_SETTINGS = (1, 3)

    # Errors
    sample_number = len(final_assembly_dict.keys())
    if sample_number > 96:
        raise ValueError('Final assembly nummber cannot exceed 96.')

    # Tips and pipette
    slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
    tipracks = [labware.load(tiprack_type, slot)
                for slot in slots]
    pipette = instruments.P10_Single(mount=PIPETTE_MOUNT, tip_racks=tipracks)

    # Define Labware and set temperature
    magbead_plate = labware.load(MAG_PLATE_TYPE, MAG_PLATE_POSITION)
    tube_rack = labware.load(TUBE_RACK_TYPE, TUBE_RACK_POSITION)
    tempdeck = modules.load('tempdeck', TEMPDECK_SLOT)
    destination_plate = labware.load(
        DESTINATION_PLATE_TYPE, TEMPDECK_SLOT, share=True)
    tempdeck.set_temperature(TEMP)
    tempdeck.wait_for_temp()

    # Master mix transfers
    final_assembly_lens = []
    for values in final_assembly_dict.values():
        final_assembly_lens.append(len(values))
    unique_assemblies_lens = list(set(final_assembly_lens))
    master_mix_well_letters = ['A', 'B', 'C', 'D']
    for x in unique_assemblies_lens:
        master_mix_well = master_mix_well_letters[(x - 1) // 6] + str(x - 1)
        destination_inds = [i for i, lens in enumerate(
            final_assembly_lens) if lens == x]
        destination_wells = np.array(
            [key for key, value in list(final_assembly_dict.items())])
        destination_wells = list(destination_wells[destination_inds])
        pipette.pick_up_tip()
        pipette.transfer(TOTAL_VOL - x * PART_VOL, tube_rack.wells(master_mix_well),
                         destination_plate.wells(destination_wells),
                         new_tip='never')
        pipette.drop_tip()

    # Part transfers
    for key, values in list(final_assembly_dict.items()):
        pipette.transfer(PART_VOL, magbead_plate.wells(values),
                         destination_plate.wells(key), mix_after=MIX_SETTINGS,
                         new_tip='always')

    tempdeck.deactivate()


final_assembly(final_assembly_dict=final_assembly_dict,
               tiprack_num=tiprack_num)

for c in robot.commands():
    print(c)
