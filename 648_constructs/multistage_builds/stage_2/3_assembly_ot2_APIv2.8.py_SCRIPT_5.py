from opentrons import protocol_api
import numpy as np
# metadata
metadata = {
'protocolName': 'My Protocol',
'description': 'Simple protocol to get started using OT2',
'apiLevel': '2.8'
}

# protocol run function. the part after the colon lets your editor know


# test dict can be used for simulation
#final_assembly_dict={ "A1": ['A7', 'B7', 'C7', 'F7'], "B1": ['A7', 'B7', 'D7', 'G7'], "C1": ['A7', 'B7', 'E7', 'H7']}
#tiprack_num=1
final_assembly_dict={"A1": [["A1", "E6", "D10"], [1, 2, 1]], "B1": [["A1", "E6", "E10"], [1, 2, 1]], "C1": [["A1", "E6", "F10"], [1, 2, 1]], "D1": [["A1", "F6", "F9"], [1, 2, 1]], "E1": [["A1", "F6", "G9"], [1, 2, 1]], "F1": [["A1", "F6", "H9"], [1, 2, 1]], "G1": [["A1", "F6", "A10"], [1, 2, 1]], "H1": [["A1", "F6", "B10"], [1, 2, 1]], "A2": [["A1", "F6", "C10"], [1, 2, 1]], "B2": [["A1", "F6", "D10"], [1, 2, 1]], "C2": [["A1", "F6", "E10"], [1, 2, 1]], "D2": [["A1", "F6", "F10"], [1, 2, 1]], "E2": [["A1", "G6", "F9"], [1, 2, 1]], "F2": [["A1", "G6", "G9"], [1, 2, 1]], "G2": [["A1", "G6", "H9"], [1, 2, 1]], "H2": [["B1", "G6", "A10"], [1, 2, 1]], "A3": [["B1", "G6", "B10"], [1, 2, 1]], "B3": [["B1", "G6", "C10"], [1, 2, 1]], "C3": [["B1", "G6", "D10"], [1, 2, 1]], "D3": [["B1", "G6", "E10"], [1, 2, 1]], "E3": [["B1", "G6", "F10"], [1, 2, 1]], "F3": [["B1", "H6", "B11"], [1, 2, 1]], "G3": [["B1", "H6", "C11"], [1, 2, 1]], "H3": [["B1", "H6", "D11"], [1, 2, 1]], "A4": [["B1", "H6", "E11"], [1, 2, 1]], "B4": [["B1", "H6", "F11"], [1, 2, 1]], "C4": [["B1", "H6", "G11"], [1, 2, 1]], "D4": [["B1", "H6", "H11"], [1, 2, 1]], "E4": [["B1", "H6", "A12"], [1, 2, 1]], "F4": [["B1", "H6", "B12"], [1, 2, 1]], "G4": [["C1", "A7", "B11"], [1, 2, 1]], "H4": [["C1", "A7", "C11"], [1, 2, 1]], "A5": [["C1", "A7", "D11"], [1, 2, 1]], "B5": [["C1", "A7", "E11"], [1, 2, 1]], "C5": [["C1", "A7", "F11"], [1, 2, 1]], "D5": [["C1", "A7", "G11"], [1, 2, 1]], "E5": [["C1", "A7", "H11"], [1, 2, 1]], "F5": [["C1", "A7", "A12"], [1, 2, 1]], "G5": [["C1", "A7", "B12"], [1, 2, 1]], "H5": [["C1", "B7", "B11"], [1, 2, 1]], "A6": [["C1", "B7", "C11"], [1, 2, 1]], "B6": [["C1", "B7", "D11"], [1, 2, 1]], "C6": [["C1", "B7", "E11"], [1, 2, 1]], "D6": [["C1", "B7", "F11"], [1, 2, 1]], "E6": [["C1", "B7", "G11"], [1, 2, 1]], "F6": [["D1", "B7", "H11"], [1, 2, 1]], "G6": [["D1", "B7", "A12"], [1, 2, 1]], "H6": [["D1", "B7", "B12"], [1, 2, 1]], "A7": [["D1", "C7", "F12"], [1, 2, 1]], "B7": [["D1", "C7", "G12"], [1, 2, 1]], "C7": [["D1", "C7", "H12"], [1, 2, 1]], "D7": [["D1", "C7", "A1"], [1, 2, 2]], "E7": [["D1", "C7", "B1"], [1, 2, 2]], "F7": [["D1", "C7", "C1"], [1, 2, 2]], "G7": [["D1", "C7", "D1"], [1, 2, 2]], "H7": [["D1", "C7", "E1"], [1, 2, 2]], "A8": [["D1", "C7", "F1"], [1, 2, 2]], "B8": [["D1", "D7", "F12"], [1, 2, 1]], "C8": [["D1", "D7", "G12"], [1, 2, 1]], "D8": [["D1", "D7", "H12"], [1, 2, 1]], "E8": [["E1", "D7", "A1"], [1, 2, 2]], "F8": [["E1", "D7", "B1"], [1, 2, 2]], "G8": [["E1", "D7", "C1"], [1, 2, 2]], "H8": [["E1", "D7", "D1"], [1, 2, 2]], "A9": [["E1", "D7", "E1"], [1, 2, 2]], "B9": [["E1", "D7", "F1"], [1, 2, 2]], "C9": [["E1", "E7", "F12"], [1, 2, 1]], "D9": [["E1", "E7", "G12"], [1, 2, 1]], "E9": [["E1", "E7", "H12"], [1, 2, 1]], "F9": [["E1", "E7", "A1"], [1, 2, 2]], "G9": [["E1", "E7", "B1"], [1, 2, 2]], "H9": [["E1", "E7", "C1"], [1, 2, 2]], "A10": [["E1", "E7", "D1"], [1, 2, 2]], "B10": [["E1", "E7", "E1"], [1, 2, 2]], "C10": [["E1", "E7", "F1"], [1, 2, 2]], "D10": [["F1", "F7", "B2"], [1, 2, 2]], "E10": [["F1", "F7", "C2"], [1, 2, 2]], "F10": [["F1", "F7", "D2"], [1, 2, 2]], "G10": [["F1", "F7", "E2"], [1, 2, 2]], "H10": [["F1", "F7", "F2"], [1, 2, 2]], "A11": [["F1", "F7", "G2"], [1, 2, 2]], "B11": [["F1", "F7", "H2"], [1, 2, 2]], "C11": [["F1", "F7", "A3"], [1, 2, 2]], "D11": [["F1", "F7", "B3"], [1, 2, 2]], "E11": [["F1", "G7", "B2"], [1, 2, 2]], "F11": [["F1", "G7", "C2"], [1, 2, 2]], "G11": [["F1", "G7", "D2"], [1, 2, 2]], "H11": [["F1", "G7", "E2"], [1, 2, 2]], "A12": [["F1", "G7", "F2"], [1, 2, 2]], "B12": [["F1", "G7", "G2"], [1, 2, 2]], "C12": [["G1", "G7", "H2"], [1, 2, 2]], "D12": [["G1", "G7", "A3"], [1, 2, 2]], "E12": [["G1", "G7", "B3"], [1, 2, 2]], "F12": [["G1", "H7", "B2"], [1, 2, 2]], "G12": [["G1", "H7", "C2"], [1, 2, 2]], "H12": [["G1", "H7", "D2"], [1, 2, 2]]}
tiprack_num=4

#tiprack_num=1
def run(protocol: protocol_api.ProtocolContext):
    def final_assembly(final_assembly_dict, tiprack_num, tiprack_type="opentrons_96_tiprack_20ul"):
            # Constants, we update all the labware name in version 2
            #Tiprack
            CANDIDATE_TIPRACK_SLOTS = ['3', '6', '9', '2', '5', '8', '11']
            PIPETTE_MOUNT = 'right'
            #Plate of sample after  purification
            MAG_PLATE_TYPE = '4ti0960rig_96_wellplate_200ul'
            MAG_PLATE_POSITION = '1'
            #Tuberack
            TUBE_RACK_TYPE = 'e14151500starlab_24_tuberack_1500ul'
            TUBE_RACK_POSITION = '7'
            #Destination plate
            DESTINATION_PLATE_TYPE = '4ti0960rig_96_wellplate_200ul'
            #Temperature control plate
            TEMPDECK_SLOT = '4'
            TEMP = 20
            TOTAL_VOL = 15
            PART_VOL = 1.5
            MIX_SETTINGS = (1, 3)
            tiprack_num=tiprack_num+1
            # Errors
            sample_number = len(final_assembly_dict.keys())
            if sample_number > 96:
                raise ValueError('Final assembly nummber cannot exceed 96.')

            slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
            tipracks = [protocol.load_labware(tiprack_type, slot) for slot in slots]
            pipette = protocol.load_instrument('p20_single_gen2', PIPETTE_MOUNT, tip_racks=tipracks)


            # Define Labware and set temperature
            magbead_plate = protocol.load_labware(MAG_PLATE_TYPE, MAG_PLATE_POSITION)
            tube_rack = protocol.load_labware(TUBE_RACK_TYPE, TUBE_RACK_POSITION)
            tempdeck = protocol.load_module('tempdeck', TEMPDECK_SLOT)
            destination_plate = tempdeck.load_labware(
            DESTINATION_PLATE_TYPE, TEMPDECK_SLOT)
            tempdeck.set_temperature(TEMP)

             # Master mix transfers
            final_assembly_lens = []
            for values in final_assembly_dict.values():
                final_assembly_lens.append(len(values))
            unique_assemblies_lens = list(set(final_assembly_lens))
            master_mix_well_letters = ['A', 'B', 'C', 'D']
            for x in unique_assemblies_lens:
                master_mix_well = master_mix_well_letters[(x - 1) // 6] + str(x - 1)
                destination_inds = [i for i, lens in enumerate(final_assembly_lens) if lens == x]
                destination_wells = np.array([key for key, value in list(final_assembly_dict.items())])
                destination_wells = list(destination_wells[destination_inds])
                for destination_well in destination_wells:# make tube_rack_wells and destination_plate.wells in the same type
                    pipette.pick_up_tip()
                    pipette.transfer(TOTAL_VOL - x * PART_VOL, tube_rack.wells(master_mix_well),
                                     destination_plate.wells(destination_well), new_tip='never')#transfer water and buffer in the pipette

                    pipette.drop_tip()

            # Part transfers
            for key, values in list(final_assembly_dict.items()):
                for value in values:# magbead_plate.wells and destination_plate.wells in the same type
                    pipette.transfer(PART_VOL, magbead_plate.wells(value),
                                     destination_plate.wells(key), mix_after=MIX_SETTINGS,
                                     new_tip='always')#transfer parts in one tube

            tempdeck.deactivate() #stop increasing the temperature

    final_assembly(final_assembly_dict=final_assembly_dict, tiprack_num=tiprack_num)
