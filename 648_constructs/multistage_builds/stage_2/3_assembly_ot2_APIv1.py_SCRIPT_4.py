from opentrons import labware, instruments, modules, robot
import numpy as np


final_assembly_dict={"A1": [["A1", "C5", "F12"], [1, 2, 1]], "B1": [["A1", "C5", "G12"], [1, 2, 1]], "C1": [["A1", "C5", "H12"], [1, 2, 1]], "D1": [["A1", "C5", "A1"], [1, 2, 2]], "E1": [["A1", "C5", "B1"], [1, 2, 2]], "F1": [["A1", "C5", "C1"], [1, 2, 2]], "G1": [["A1", "C5", "D1"], [1, 2, 2]], "H1": [["A1", "C5", "E1"], [1, 2, 2]], "A2": [["A1", "C5", "F1"], [1, 2, 2]], "B2": [["A1", "D5", "B2"], [1, 2, 2]], "C2": [["A1", "D5", "C2"], [1, 2, 2]], "D2": [["A1", "D5", "D2"], [1, 2, 2]], "E2": [["A1", "D5", "E2"], [1, 2, 2]], "F2": [["A1", "D5", "F2"], [1, 2, 2]], "G2": [["A1", "D5", "G2"], [1, 2, 2]], "H2": [["B1", "D5", "H2"], [1, 2, 2]], "A3": [["B1", "D5", "A3"], [1, 2, 2]], "B3": [["B1", "D5", "B3"], [1, 2, 2]], "C3": [["B1", "E5", "B2"], [1, 2, 2]], "D3": [["B1", "E5", "C2"], [1, 2, 2]], "E3": [["B1", "E5", "D2"], [1, 2, 2]], "F3": [["B1", "E5", "E2"], [1, 2, 2]], "G3": [["B1", "E5", "F2"], [1, 2, 2]], "H3": [["B1", "E5", "G2"], [1, 2, 2]], "A4": [["B1", "E5", "H2"], [1, 2, 2]], "B4": [["B1", "E5", "A3"], [1, 2, 2]], "C4": [["B1", "E5", "B3"], [1, 2, 2]], "D4": [["B1", "F5", "B2"], [1, 2, 2]], "E4": [["B1", "F5", "C2"], [1, 2, 2]], "F4": [["B1", "F5", "D2"], [1, 2, 2]], "G4": [["C1", "F5", "E2"], [1, 2, 2]], "H4": [["C1", "F5", "F2"], [1, 2, 2]], "A5": [["C1", "F5", "G2"], [1, 2, 2]], "B5": [["C1", "F5", "H2"], [1, 2, 2]], "C5": [["C1", "F5", "A3"], [1, 2, 2]], "D5": [["C1", "F5", "B3"], [1, 2, 2]], "E5": [["C1", "G5", "F6"], [1, 2, 1]], "F5": [["C1", "G5", "G6"], [1, 2, 1]], "G5": [["C1", "G5", "H6"], [1, 2, 1]], "H5": [["C1", "G5", "A7"], [1, 2, 1]], "A6": [["C1", "G5", "B7"], [1, 2, 1]], "B6": [["C1", "G5", "C7"], [1, 2, 1]], "C6": [["C1", "G5", "D7"], [1, 2, 1]], "D6": [["C1", "G5", "E7"], [1, 2, 1]], "E6": [["C1", "G5", "F7"], [1, 2, 1]], "F6": [["D1", "H5", "F6"], [1, 2, 1]], "G6": [["D1", "H5", "G6"], [1, 2, 1]], "H6": [["D1", "H5", "H6"], [1, 2, 1]], "A7": [["D1", "H5", "A7"], [1, 2, 1]], "B7": [["D1", "H5", "B7"], [1, 2, 1]], "C7": [["D1", "H5", "C7"], [1, 2, 1]], "D7": [["D1", "H5", "D7"], [1, 2, 1]], "E7": [["D1", "H5", "E7"], [1, 2, 1]], "F7": [["D1", "H5", "F7"], [1, 2, 1]], "G7": [["D1", "A6", "F6"], [1, 2, 1]], "H7": [["D1", "A6", "G6"], [1, 2, 1]], "A8": [["D1", "A6", "H6"], [1, 2, 1]], "B8": [["D1", "A6", "A7"], [1, 2, 1]], "C8": [["D1", "A6", "B7"], [1, 2, 1]], "D8": [["D1", "A6", "C7"], [1, 2, 1]], "E8": [["E1", "A6", "D7"], [1, 2, 1]], "F8": [["E1", "A6", "E7"], [1, 2, 1]], "G8": [["E1", "A6", "F7"], [1, 2, 1]], "H8": [["E1", "B6", "B8"], [1, 2, 1]], "A9": [["E1", "B6", "C8"], [1, 2, 1]], "B9": [["E1", "B6", "D8"], [1, 2, 1]], "C9": [["E1", "B6", "E8"], [1, 2, 1]], "D9": [["E1", "B6", "F8"], [1, 2, 1]], "E9": [["E1", "B6", "G8"], [1, 2, 1]], "F9": [["E1", "B6", "H8"], [1, 2, 1]], "G9": [["E1", "B6", "A9"], [1, 2, 1]], "H9": [["E1", "B6", "B9"], [1, 2, 1]], "A10": [["E1", "C6", "B8"], [1, 2, 1]], "B10": [["E1", "C6", "C8"], [1, 2, 1]], "C10": [["E1", "C6", "D8"], [1, 2, 1]], "D10": [["F1", "C6", "E8"], [1, 2, 1]], "E10": [["F1", "C6", "F8"], [1, 2, 1]], "F10": [["F1", "C6", "G8"], [1, 2, 1]], "G10": [["F1", "C6", "H8"], [1, 2, 1]], "H10": [["F1", "C6", "A9"], [1, 2, 1]], "A11": [["F1", "C6", "B9"], [1, 2, 1]], "B11": [["F1", "D6", "B8"], [1, 2, 1]], "C11": [["F1", "D6", "C8"], [1, 2, 1]], "D11": [["F1", "D6", "D8"], [1, 2, 1]], "E11": [["F1", "D6", "E8"], [1, 2, 1]], "F11": [["F1", "D6", "F8"], [1, 2, 1]], "G11": [["F1", "D6", "G8"], [1, 2, 1]], "H11": [["F1", "D6", "H8"], [1, 2, 1]], "A12": [["F1", "D6", "A9"], [1, 2, 1]], "B12": [["F1", "D6", "B9"], [1, 2, 1]], "C12": [["G1", "E6", "F9"], [1, 2, 1]], "D12": [["G1", "E6", "G9"], [1, 2, 1]], "E12": [["G1", "E6", "H9"], [1, 2, 1]], "F12": [["G1", "E6", "A10"], [1, 2, 1]], "G12": [["G1", "E6", "B10"], [1, 2, 1]], "H12": [["G1", "E6", "C10"], [1, 2, 1]]}
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
