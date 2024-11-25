from opentrons import labware, instruments, modules, robot
import numpy as np


final_assembly_dict={"A1": [["E5", "F8", "C3"], [1, 2, 2]], "B1": [["F5", "F8", "D3"], [1, 2, 2]], "C1": [["F5", "F8", "E3"], [1, 2, 2]], "D1": [["F5", "F8", "F3"], [1, 2, 2]], "E1": [["F5", "F8", "G3"], [1, 2, 2]], "F1": [["F5", "F8", "H3"], [1, 2, 2]], "G1": [["F5", "G8", "D7"], [1, 2, 1]], "H1": [["F5", "G8", "E7"], [1, 2, 1]], "A2": [["F5", "G8", "F7"], [1, 2, 1]], "B2": [["F5", "G8", "G7"], [1, 2, 1]], "C2": [["F5", "G8", "H7"], [1, 2, 1]], "D2": [["F5", "G8", "A8"], [1, 2, 1]], "E2": [["F5", "G8", "B8"], [1, 2, 1]], "F2": [["F5", "G8", "C8"], [1, 2, 1]], "G2": [["G5", "G8", "D8"], [1, 2, 1]], "H2": [["G5", "H8", "D7"], [1, 2, 1]], "A3": [["G5", "H8", "E7"], [1, 2, 1]], "B3": [["G5", "H8", "F7"], [1, 2, 1]], "C3": [["G5", "H8", "G7"], [1, 2, 1]], "D3": [["G5", "H8", "H7"], [1, 2, 1]], "E3": [["G5", "H8", "A8"], [1, 2, 1]], "F3": [["G5", "H8", "B8"], [1, 2, 1]], "G3": [["G5", "H8", "C8"], [1, 2, 1]], "H3": [["G5", "H8", "D8"], [1, 2, 1]], "A4": [["G5", "A9", "D7"], [1, 2, 1]], "B4": [["G5", "A9", "E7"], [1, 2, 1]], "C4": [["G5", "A9", "F7"], [1, 2, 1]], "D4": [["H5", "A9", "G7"], [1, 2, 1]], "E4": [["H5", "A9", "H7"], [1, 2, 1]], "F4": [["H5", "A9", "A8"], [1, 2, 1]], "G4": [["H5", "A9", "B8"], [1, 2, 1]], "H4": [["H5", "A9", "C8"], [1, 2, 1]], "A5": [["H5", "A9", "D8"], [1, 2, 1]], "B5": [["H5", "B9", "H8"], [1, 2, 1]], "C5": [["H5", "B9", "A9"], [1, 2, 1]], "D5": [["H5", "B9", "B9"], [1, 2, 1]], "E5": [["H5", "B9", "C9"], [1, 2, 1]], "F5": [["H5", "B9", "D9"], [1, 2, 1]], "G5": [["H5", "B9", "E9"], [1, 2, 1]], "H5": [["H5", "B9", "F9"], [1, 2, 1]], "A6": [["A6", "B9", "G9"], [1, 2, 1]], "B6": [["A6", "B9", "H9"], [1, 2, 1]], "C6": [["A6", "C9", "H8"], [1, 2, 1]], "D6": [["A6", "C9", "A9"], [1, 2, 1]], "E6": [["A6", "C9", "B9"], [1, 2, 1]], "F6": [["A6", "C9", "C9"], [1, 2, 1]], "G6": [["A6", "C9", "D9"], [1, 2, 1]], "H6": [["A6", "C9", "E9"], [1, 2, 1]], "A7": [["A6", "C9", "F9"], [1, 2, 1]], "B7": [["A6", "C9", "G9"], [1, 2, 1]], "C7": [["A6", "C9", "H9"], [1, 2, 1]], "D7": [["A6", "D9", "H8"], [1, 2, 1]], "E7": [["A6", "D9", "A9"], [1, 2, 1]], "F7": [["B6", "D9", "B9"], [1, 2, 1]], "G7": [["B6", "D9", "C9"], [1, 2, 1]], "H7": [["B6", "D9", "D9"], [1, 2, 1]], "A8": [["B6", "D9", "E9"], [1, 2, 1]], "B8": [["B6", "D9", "F9"], [1, 2, 1]], "C8": [["B6", "D9", "G9"], [1, 2, 1]], "D8": [["B6", "D9", "H9"], [1, 2, 1]], "E8": [["B6", "E9", "D10"], [1, 2, 1]], "F8": [["B6", "E9", "E10"], [1, 2, 1]], "G8": [["B6", "E9", "F10"], [1, 2, 1]], "H8": [["B6", "E9", "G10"], [1, 2, 1]], "A9": [["B6", "E9", "H10"], [1, 2, 1]], "B9": [["B6", "E9", "A11"], [1, 2, 1]], "C9": [["C6", "E9", "B11"], [1, 2, 1]], "D9": [["C6", "E9", "C11"], [1, 2, 1]], "E9": [["C6", "E9", "D11"], [1, 2, 1]], "F9": [["C6", "F9", "D10"], [1, 2, 1]], "G9": [["C6", "F9", "E10"], [1, 2, 1]], "H9": [["C6", "F9", "F10"], [1, 2, 1]], "A10": [["C6", "F9", "G10"], [1, 2, 1]], "B10": [["C6", "F9", "H10"], [1, 2, 1]], "C10": [["C6", "F9", "A11"], [1, 2, 1]], "D10": [["C6", "F9", "B11"], [1, 2, 1]], "E10": [["C6", "F9", "C11"], [1, 2, 1]], "F10": [["C6", "F9", "D11"], [1, 2, 1]], "G10": [["C6", "G9", "D10"], [1, 2, 1]], "H10": [["D6", "G9", "E10"], [1, 2, 1]], "A11": [["D6", "G9", "F10"], [1, 2, 1]], "B11": [["D6", "G9", "G10"], [1, 2, 1]], "C11": [["D6", "G9", "H10"], [1, 2, 1]], "D11": [["D6", "G9", "A11"], [1, 2, 1]], "E11": [["D6", "G9", "B11"], [1, 2, 1]], "F11": [["D6", "G9", "C11"], [1, 2, 1]], "G11": [["D6", "G9", "D11"], [1, 2, 1]], "H11": [["D6", "H9", "H11"], [1, 2, 1]], "A12": [["D6", "H9", "A12"], [1, 2, 1]], "B12": [["D6", "H9", "B12"], [1, 2, 1]], "C12": [["D6", "H9", "C12"], [1, 2, 1]], "D12": [["D6", "H9", "D12"], [1, 2, 1]], "E12": [["E6", "H9", "E12"], [1, 2, 1]], "F12": [["E6", "H9", "F12"], [1, 2, 1]], "G12": [["E6", "H9", "G12"], [1, 2, 1]], "H12": [["E6", "H9", "H12"], [1, 2, 1]]}
tiprack_num=4


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
