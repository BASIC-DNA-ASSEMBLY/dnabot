from __future__ import unicode_literals
from opentrons import protocol_api
import numpy as np
# metadata
metadata = {
'protocolName': 'DNABOT Assembly Thermocycler',
'description': 'DNABOT Assembly Step3 with Thermocycler',
'apiLevel': '2.8'
}

# It is possible to run 88 assemblies with this new module. The heat block module is removed. 
# Assembly reactions is set up on thermocycler module.


# test dictionary can be used for simulation 3 or 88 assemblies
final_assembly_dict={"A1": [['A7', 'B7', 'C7', 'F7'], [1, 2, 1, 1]], "B1": [['A7', 'B7', 'D7', 'G7'], [1, 2, 1, 1]], "C1": [['A7', 'E7', 'H7'], [1, 2, 1]]}
tiprack_num=1

# final_assembly_dict={"A1": [["A1", "C9", "B11"], [1, 2, 1]], "B1": [["A1", "C9", "C11"], [1, 2, 1]], "C1": [["A1", "C9", "D11"], [1, 2, 1]], "D1": [["A1", "C9", "E11"], [1, 2, 1]], "E1": [["A1", "C9", "F11"], [1, 2, 1]], "F1": [["A1", "C9", "G11"], [1, 2, 1]], "G1": [["A1", "C9", "H11"], [1, 2, 1]], "H1": [["A1", "C9", "A12"], [1, 2, 1]], "A2": [["A1", "C9", "B12"], [1, 2, 1]], "B2": [["A1", "D9", "B11"], [1, 2, 1]], "C2": [["A1", "D9", "C11"], [1, 2, 1]], "D2": [["A1", "D9", "D11"], [1, 2, 1]], "E2": [["A1", "D9", "E11"], [1, 2, 1]], "F2": [["A1", "D9", "F11"], [1, 2, 1]], "G2": [["A1", "D9", "G11"], [1, 2, 1]], "H2": [["B1", "D9", "H11"], [1, 2, 1]], "A3": [["B1", "D9", "A12"], [1, 2, 1]], "B3": [["B1", "D9", "B12"], [1, 2, 1]], "C3": [["B1", "E9", "F12"], [1, 2, 1]], "D3": [["B1", "E9", "G12"], [1, 2, 1]], "E3": [["B1", "E9", "H12"], [1, 2, 1]], "F3": [["B1", "E9", "A1"], [1, 2, 2]], "G3": [["B1", "E9", "B1"], [1, 2, 2]], "H3": [["B1", "E9", "C1"], [1, 2, 2]], "A4": [["B1", "E9", "D1"], [1, 2, 2]], "B4": [["B1", "E9", "E1"], [1, 2, 2]], "C4": [["B1", "E9", "F1"], [1, 2, 2]], "D4": [["B1", "F9", "F12"], [1, 2, 1]], "E4": [["B1", "F9", "G12"], [1, 2, 1]], "F4": [["B1", "F9", "H12"], [1, 2, 1]], "G4": [["C1", "F9", "A1"], [1, 2, 2]], "H4": [["C1", "F9", "B1"], [1, 2, 2]], "A5": [["C1", "F9", "C1"], [1, 2, 2]], "B5": [["C1", "F9", "D1"], [1, 2, 2]], "C5": [["C1", "F9", "E1"], [1, 2, 2]], "D5": [["C1", "F9", "F1"], [1, 2, 2]], "E5": [["C1", "G9", "F12"], [1, 2, 1]], "F5": [["C1", "G9", "G12"], [1, 2, 1]], "G5": [["C1", "G9", "H12"], [1, 2, 1]], "H5": [["C1", "G9", "A1"], [1, 2, 2]], "A6": [["C1", "G9", "B1"], [1, 2, 2]], "B6": [["C1", "G9", "C1"], [1, 2, 2]], "C6": [["C1", "G9", "D1"], [1, 2, 2]], "D6": [["C1", "G9", "E1"], [1, 2, 2]], "E6": [["C1", "G9", "F1"], [1, 2, 2]], "F6": [["D1", "H9", "B2"], [1, 2, 2]], "G6": [["D1", "H9", "C2"], [1, 2, 2]], "H6": [["D1", "H9", "D2"], [1, 2, 2]], "A7": [["D1", "H9", "E2"], [1, 2, 2]], "B7": [["D1", "H9", "F2"], [1, 2, 2]], "C7": [["D1", "H9", "G2"], [1, 2, 2]], "D7": [["D1", "H9", "H2"], [1, 2, 2]], "E7": [["D1", "H9", "A3"], [1, 2, 2]], "F7": [["D1", "H9", "B3"], [1, 2, 2]], "G7": [["D1", "A10", "B2"], [1, 2, 2]], "H7": [["D1", "A10", "C2"], [1, 2, 2]], "A8": [["D1", "A10", "D2"], [1, 2, 2]], "B8": [["D1", "A10", "E2"], [1, 2, 2]], "C8": [["D1", "A10", "F2"], [1, 2, 2]], "D8": [["D1", "A10", "G2"], [1, 2, 2]], "E8": [["E1", "A10", "H2"], [1, 2, 2]], "F8": [["E1", "A10", "A3"], [1, 2, 2]], "G8": [["E1", "A10", "B3"], [1, 2, 2]], "H8": [["E1", "B10", "B2"], [1, 2, 2]], "A9": [["E1", "B10", "C2"], [1, 2, 2]], "B9": [["E1", "B10", "D2"], [1, 2, 2]], "C9": [["E1", "B10", "E2"], [1, 2, 2]], "D9": [["E1", "B10", "F2"], [1, 2, 2]], "E9": [["E1", "B10", "G2"], [1, 2, 2]], "F9": [["E1", "B10", "H2"], [1, 2, 2]], "G9": [["E1", "B10", "A3"], [1, 2, 2]], "H9": [["E1", "B10", "B3"], [1, 2, 2]]}
# tiprack_num=3

# opentrons_simulate.exe dnabot\template_ot2_scripts\assembly_template_Thermocycler_module_APIv2.8.py --custom-labware-path 'labware\Labware definitions'

final_assembly_dict={"A1": [["E2", "H3", "E8"], [1, 2, 1]], "B1": [["E2", "H3", "F8"], [1, 2, 1]], "C1": [["E2", "H3", "G8"], [1, 2, 1]], "D1": [["F2", "H3", "H8"], [1, 2, 1]], "E1": [["F2", "H3", "A9"], [1, 2, 1]], "F1": [["F2", "H3", "B9"], [1, 2, 1]], "G1": [["F2", "A4", "B8"], [1, 2, 1]], "H1": [["F2", "A4", "C8"], [1, 2, 1]], "A2": [["F2", "A4", "D8"], [1, 2, 1]], "B2": [["F2", "A4", "E8"], [1, 2, 1]], "C2": [["F2", "A4", "F8"], [1, 2, 1]], "D2": [["F2", "A4", "G8"], [1, 2, 1]], "E2": [["F2", "A4", "H8"], [1, 2, 1]], "F2": [["F2", "A4", "A9"], [1, 2, 1]], "G2": [["F2", "A4", "B9"], [1, 2, 1]], "H2": [["F2", "B4", "B8"], [1, 2, 1]], "A3": [["F2", "B4", "C8"], [1, 2, 1]], "B3": [["F2", "B4", "D8"], [1, 2, 1]], "C3": [["G2", "B4", "E8"], [1, 2, 1]], "D3": [["G2", "B4", "F8"], [1, 2, 1]], "E3": [["G2", "B4", "G8"], [1, 2, 1]], "F3": [["G2", "B4", "H8"], [1, 2, 1]], "G3": [["G2", "B4", "A9"], [1, 2, 1]], "H3": [["G2", "B4", "B9"], [1, 2, 1]], "A4": [["G2", "C4", "F9"], [1, 2, 1]], "B4": [["G2", "C4", "G9"], [1, 2, 1]], "C4": [["G2", "C4", "H9"], [1, 2, 1]], "D4": [["G2", "C4", "A10"], [1, 2, 1]], "E4": [["G2", "C4", "B10"], [1, 2, 1]], "F4": [["G2", "C4", "C10"], [1, 2, 1]], "G4": [["G2", "C4", "D10"], [1, 2, 1]], "H4": [["G2", "C4", "E10"], [1, 2, 1]], "A5": [["G2", "C4", "F10"], [1, 2, 1]], "B5": [["H2", "D4", "F9"], [1, 2, 1]], "C5": [["H2", "D4", "G9"], [1, 2, 1]], "D5": [["H2", "D4", "H9"], [1, 2, 1]], "E5": [["H2", "D4", "A10"], [1, 2, 1]], "F5": [["H2", "D4", "B10"], [1, 2, 1]], "G5": [["H2", "D4", "C10"], [1, 2, 1]], "H5": [["H2", "D4", "D10"], [1, 2, 1]], "A6": [["H2", "D4", "E10"], [1, 2, 1]], "B6": [["H2", "D4", "F10"], [1, 2, 1]], "C6": [["H2", "E4", "F9"], [1, 2, 1]], "D6": [["H2", "E4", "G9"], [1, 2, 1]], "E6": [["H2", "E4", "H9"], [1, 2, 1]], "F6": [["H2", "E4", "A10"], [1, 2, 1]], "G6": [["H2", "E4", "B10"], [1, 2, 1]], "H6": [["H2", "E4", "C10"], [1, 2, 1]], "A7": [["A3", "E4", "D10"], [1, 2, 1]], "B7": [["A3", "E4", "E10"], [1, 2, 1]], "C7": [["A3", "E4", "F10"], [1, 2, 1]], "D7": [["A3", "F4", "B11"], [1, 2, 1]], "E7": [["A3", "F4", "C11"], [1, 2, 1]], "F7": [["A3", "F4", "D11"], [1, 2, 1]], "G7": [["A3", "F4", "E11"], [1, 2, 1]], "H7": [["A3", "F4", "F11"], [1, 2, 1]], "A8": [["A3", "F4", "G11"], [1, 2, 1]], "B8": [["A3", "F4", "H11"], [1, 2, 1]], "C8": [["A3", "F4", "A12"], [1, 2, 1]], "D8": [["A3", "F4", "B12"], [1, 2, 1]], "E8": [["A3", "G4", "B11"], [1, 2, 1]], "F8": [["A3", "G4", "C11"], [1, 2, 1]], "G8": [["A3", "G4", "D11"], [1, 2, 1]], "H8": [["B3", "G4", "E11"], [1, 2, 1]], "A9": [["B3", "G4", "F11"], [1, 2, 1]], "B9": [["B3", "G4", "G11"], [1, 2, 1]], "C9": [["B3", "G4", "H11"], [1, 2, 1]], "D9": [["B3", "G4", "A12"], [1, 2, 1]], "E9": [["B3", "G4", "B12"], [1, 2, 1]], "F9": [["B3", "H4", "B11"], [1, 2, 1]], "G9": [["B3", "H4", "C11"], [1, 2, 1]], "H9": [["B3", "H4", "D11"], [1, 2, 1]], "A10": [["B3", "H4", "E11"], [1, 2, 1]], "B10": [["B3", "H4", "F11"], [1, 2, 1]], "C10": [["B3", "H4", "G11"], [1, 2, 1]], "D10": [["B3", "H4", "H11"], [1, 2, 1]], "E10": [["B3", "H4", "A12"], [1, 2, 1]], "F10": [["B3", "H4", "B12"], [1, 2, 1]], "G10": [["C3", "A5", "F12"], [1, 2, 1]], "H10": [["C3", "A5", "G12"], [1, 2, 1]], "A11": [["C3", "A5", "H12"], [1, 2, 1]], "B11": [["C3", "A5", "A1"], [1, 2, 2]], "C11": [["C3", "A5", "B1"], [1, 2, 2]], "D11": [["C3", "A5", "C1"], [1, 2, 2]], "E11": [["C3", "A5", "D1"], [1, 2, 2]], "F11": [["C3", "A5", "E1"], [1, 2, 2]], "G11": [["C3", "A5", "F1"], [1, 2, 2]], "H11": [["C3", "B5", "F12"], [1, 2, 1]], "A12": [["C3", "B5", "G12"], [1, 2, 1]], "B12": [["C3", "B5", "H12"], [1, 2, 1]], "C12": [["C3", "B5", "A1"], [1, 2, 2]], "D12": [["C3", "B5", "B1"], [1, 2, 2]], "E12": [["C3", "B5", "C1"], [1, 2, 2]], "F12": [["D3", "B5", "D1"], [1, 2, 2]], "G12": [["D3", "B5", "E1"], [1, 2, 2]], "H12": [["D3", "B5", "F1"], [1, 2, 2]]}
tiprack_num=4


def run(protocol: protocol_api.ProtocolContext):
    def final_assembly(final_assembly_dict, tiprack_num, tiprack_type="opentrons_96_tiprack_20ul"):
            ### Constants

            # Source plate(s)
            SOURCE_PLATE_TYPE = '4ti0960rig_96_wellplate_200ul'
            source_plate_list = [plate for value in final_assembly_dict.values() for plate in value[1]]     # list of source plates for all clips 
            source_plate_slots = list(set(source_plate_list))                                               # unique source plates
            source_plates = {plate: protocol.load_labware(SOURCE_PLATE_TYPE, plate) for plate in source_plate_slots}

            # Tuberack
            TUBE_RACK_TYPE = 'e14151500starlab_24_tuberack_1500ul'
            TUBE_RACK_POSITION = '4'
            tube_rack = protocol.load_labware(TUBE_RACK_TYPE, TUBE_RACK_POSITION)

            # Destination plate
            DESTINATION_PLATE_TYPE = '4ti0960rig_96_wellplate_200ul'
            TOTAL_VOL = 15
            PART_VOL = 1.5
            MIX_SETTINGS = (1, 3)
            # tiprack_num += 1                    # + 1 for one index ############################### I think(?)

            # Thermocycler Module
            try:
                tc_mod = protocol.load_module('Thermocycler Module')
            except:
                tc_mod = protocol.load_module('thermocyclerModuleV2')

            destination_plate = tc_mod.load_labware(DESTINATION_PLATE_TYPE)
            tc_mod.open_lid()
            tc_mod.set_block_temperature(20)

            # Error trapping
            sample_number = len(final_assembly_dict.keys())
            if sample_number > 96:
                raise ValueError('Final assembly nummber cannot exceed 96.')

            # Tiprack(s)
            CANDIDATE_TIPRACK_SLOTS = ['3', '5', '6', '9']

            if 2 not in source_plate_slots:                  # if only one source plate used, deck slot 2 can be used for a tip rack
                CANDIDATE_TIPRACK_SLOTS.append('2')

            if tiprack_num > len(CANDIDATE_TIPRACK_SLOTS):
                raise ValueError('Not enough tipracks available on deck to satisfy tip requirements. Consider either splitting into multiple builds each with fewer constructs or iterative rounds of building. ')
                  
            slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
            tipracks = [protocol.load_labware(tiprack_type, slot) for slot in slots]

            # Pipette
            PIPETTE_MOUNT = 'right'      
            pipette = protocol.load_instrument('p20_single_gen2', PIPETTE_MOUNT, tip_racks=tipracks)

            # Master mix transfers
            final_assembly_lens = [len(values[0]) for values in final_assembly_dict.values()]       # list of assembly lengths (number of clips)
            unique_assemblies_lens = list(set(final_assembly_lens))                                 # unique lengths

            destination_wells = np.array([key for key, value in final_assembly_dict.items()])
            
            pipette.pick_up_tip()
            for x in unique_assemblies_lens: 
                master_mix_well = tube_counter(x-2)    # select well in tube rack (-2 as one indexed and fewest clips possible is 2)
                destination_inds = [i for i, lens in enumerate(final_assembly_lens) if lens == x]   # find all assemblies of length x
                destination_wells_for_len = list(destination_wells[destination_inds])

                # # Common backbones (up to 3, else complete original way)
                # backbones = []
                # for components in final_assembly_dict.values():
                #     backbone = components[0][0]
                #     backbones.append(backbone) 
                # unique_backbones = list(set(backbones))             # NB contains multiple wells with same bb in - need method for combining 
                # print(backbones)

                # if len(unique_backbones) < 3:
                #     print('finish this part')
                #     ''''Notes
                #         The idea here was to produce a master mix for each backbone and dilution combination.
                #         I could do away with the user having to premix their own dilution of the assembly buffer
                #         and have the robot make a series of master mixes for each unique number of parts (i.e. 
                #         dilution) and backbone. This would save a lot of time and tips.

                #         This could be done by having the user make a stronger buffer and putting a limit on the 
                #         max number of parts for an assembly, or possibly better would be to have the user make 
                #         the assembly buffer tubes as required and then have the robot aliquot the master mixes 
                #         and then add backbones to each individually
                #     '''
                
                for destination_well in destination_wells_for_len: # make tube_rack_wells and destination_plate.wells in the same type
                    
                    pipette.transfer(TOTAL_VOL - x * PART_VOL, tube_rack.wells(master_mix_well),
                                     destination_plate.wells(destination_well), new_tip='never')    #transfer water and buffer in the pipette

            pipette.return_tip()
            pipette.reset_tipracks()

            # Part transfers
            for key, values in list(final_assembly_dict.items()):
                for i in range(len(values[0])):                     # find well and plate for every clip in every assembly
                    well  = values[0][i]
                    plate = values[1][i]

                    mix = (0,0)
                    if i == len(values[0])-1:                       # set to mix if on final clip transfer
                        mix = MIX_SETTINGS

                    pipette.transfer(PART_VOL, source_plates[plate].wells(well),
                                     destination_plate.wells(key), mix_after=mix, new_tip='always')

            # Thermocycler Module
            tc_mod.close_lid()
            tc_mod.set_lid_temperature(105)
            tc_mod.set_block_temperature(50, hold_time_minutes=45, block_max_volume=15)
            tc_mod.set_block_temperature(8, block_max_volume=30)
            tc_mod.set_lid_temperature(37)
            # tc_mod.open_lid()                                     # leave lid shut to prevent evaporation
        
        
    def counter(rows):

        def inner(n):
            """ Takes either a value or a well location and converts to other fomat """
            
            row_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}

            if type(n) == int:
                row = row_dict[n // rows]
                col = 1 + n % rows
                return row + f'{col}'
                # return row + f'{col:02d}' # for if 2 sf number required (i.e. 'A01' rather than 'A1')

        return inner
    tube_counter = counter(6)


    final_assembly(final_assembly_dict=final_assembly_dict, tiprack_num=tiprack_num)