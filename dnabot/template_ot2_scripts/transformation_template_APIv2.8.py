from opentrons import protocol_api
import numpy as np


# Rename to 'purification_template' and paste into 'template_ot2_scripts' folder in DNA-BOT to use


metadata = {
     'apiLevel': '2.8',
     'protocolName': 'Transformation',
     'description': 'Transformation reactions using an opentrons OT-2 for BASIC assembly.'}

# Example output produced by DNA-BOT for a single construct, uncomment and run to test the template
#spotting_tuples=[(('A1','B1','C1'), ('A1','B1', 'C1'), (5,5,5))]
#soc_well='A1'

# Example output produced by DNA-BOT for 88 constructs, uncomment and run to test the template
#spotting_tuples=[(('A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'), ('A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'), ('A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'), ('A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'), ('A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'), ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'), ('A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'), ('A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'), ('A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9'), ('A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10'), ('A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10'), (5, 5, 5, 5, 5, 5, 5, 5)), (('A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11'), ('A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11'), (5, 5, 5, 5, 5, 5, 5, 5))]
#soc_well='A1'

# __LABWARES is expected to be redefined by "generate_ot2_script" method
# Test dict
# __LABWARES={"p10_single": {"id": "p20_single_gen2"}, "p300_multi": {"id": "p300_multi_gen2"}, "mag_deck": {"id": "magdeck"}, "24_tuberack_1500ul": {"id": "e14151500starlab_24_tuberack_1500ul"}, "96_tiprack_10ul": {"id": "opentrons_96_tiprack_20ul"}, "96_tiprack_300ul": {"id": "opentrons_96_tiprack_300ul"}, "96_wellplate_200ul_pcr": {"id": "4ti0960rig_96_wellplate_200ul"}, "12_reservoir_21000ul": {"id": "4ti0131_12_reservoir_21000ul"}, "96_deepwellplate_2ml": {"id": "4ti0136_96_wellplate_2200ul"}}

def run(protocol: protocol_api.ProtocolContext):
# added run function for API version 2

# Constants
    CANDIDATE_p20_SLOTS = ['9', '2', '5']
    CANDIDATE_P300_SLOTS = ['3', '6']
    p20_TIPRACK_TYPE = __LABWARES['96_tiprack_10ul']['id']
        # changed from 'tiprack-10ul'
    P300_TIPRACK_TYPE = __LABWARES['96_tiprack_300ul']['id']
    P20_MOUNT = 'right'
    P300_MOUNT = 'left'
    ASSEMBLY_PLATE_TYPE = __LABWARES['96_wellplate_200ul_pcr']['id']
    ASSEMBLY_PLATE_SLOT = '8'

    TRANSFORMATION_PLATE_TYPE = __LABWARES['96_wellplate_200ul_pcr']['id']
    SOC_PLATE_TYPE = __LABWARES['96_deepwellplate_2ml']['id']
    SOC_PLATE_SLOT = '7'
    TUBE_RACK_TYPE = __LABWARES['24_tuberack_1500ul']['id']
    TUBE_RACK_SLOT = '11'
    SPOTTING_WASTE_WELL = 'A1'
    AGAR_PLATE_TYPE = __LABWARES['96_wellplate_200ul_pcr']['id']
        # changed from 'Nunc_Omnitray'
            # it is a 1 well plate filled with agar;
            # but for the Opentron to spot in the locations of a 96 wp, it is defined similar to a 96 wp
            # was previously defined in add.labware.py, API version 2 doesn't support labware.create anymore



        # custom labware made using Opentron's Labware Creator:
            # external dimensions:
                # footprint length = 127.76 mm
                # footrpint width = 85.48 mm
                # footprint height = 15.70 mm
                # taken from Thermofisher's documentation for Nunc Omnitray
                # https://www.thermofisher.com/document-connect/document-connect.html?url=https%3A%2F%2Fassets.thermofisher.com%2FTFS-Assets%2FLSG%2Fmanuals%2FD03023.pdf&title=VGVjaG5pY2FsIERhdGEgU2hlZXQ6IE51bmMgT21uaXRyYXk=
            # well measurements
                # depth = 0.01 mm
                # diameter =  0.01 mm
                # in old add.labware.py, they were defined as 0, but Labware Creator requires a value >0
            # spacing
                # x-offset = 14.38 mm
                # y-offset = 11.24 mm
                # x-spacing = 9.00 mm
                # y-spacing) = 9.00 mm
                # taken from Nest 96 well plates
                # https://labware.opentrons.com/nest_96_wellplate_100ul_pcr_full_skirt/
        # before using protocol, need to upload the 'nuncomnitray_96_wellplate_0.01ul.json' custom labware file into Opentrons app

    AGAR_PLATE_SLOT = '1'

    TEMPDECK_SLOT = '10'
    

    
    def generate_transformation_wells(spotting_tuples):
        """
        Evaluates spotting_tuples and returns transformation wells.

        Args:
        spotting_tuples (list): Sets of spotting reactions are given in the form: ((source wells), (target wells), (spotting volumes)).

        """

        wells = []
        for spotting_tuple in spotting_tuples:
            for source_well in spotting_tuple[0]:
                wells.append(source_well)
        transformation_wells = [well for i, well in enumerate(
            wells) if wells.index(well) == i]
        return transformation_wells


    def tiprack_slots(spotting_tuples, max_spot_vol=5):
        """
        Calculates p20 and p300 tiprack slots required.

        Args:
        spotting_tuples (list): Sets of spotting reactions are given in the form: ((source wells), (target wells), (spotting volumes)).
        max_spot_vol (float): Maximum volume that is spotted per spot reaction.

        """

        # Reactions' number
        transformation_reactions = len(generate_transformation_wells(spotting_tuples))
        spotting_reactions = 0
        for spotting_tuple in spotting_tuples:
            spots = np.array(spotting_tuple[2])/max_spot_vol
            np.ceil(spots)
            spotting_reactions = spotting_reactions + int(np.sum(spots))

        # errrr should be fine lol # REMOVE

        # p20 tiprack slots
        p20_tips = transformation_reactions + spotting_reactions
        p20_tiprack_slots = p20_tips // 96 + 1 if p20_tips % 96 > 0 else p20_tips / 96

        # p300 tiprack slots
        p300_tips = transformation_reactions + spotting_reactions
        p300_tiprack_slots = p300_tips // 96 + \
            1 if p300_tips % 96 > 0 else p300_tips / 96
        return int(p20_tiprack_slots), int(p300_tiprack_slots)


    def transformation_setup(transformation_wells):
        """
        Sets up transformation reactions

        Args:
        transformation_wells (list).

        """

        # Constants
        TEMP = 4  # Incubation temperature.
        ASSEMBLY_VOL = 5  # Volume of final assembly added to competent cells.
        MIX_SETTINGS = (4, 5)  # Mix after setting during final assembly transfers.
        INCUBATION_TIME = 20  # Cells and final assembly incubation time.



        # Set temperature deck to 4 °C and load competent cells
        tempdeck.set_temperature(TEMP)
        # removed: tempdeck.wait_for_temp()
            # API version2 automatically pauses execution until the set temperature is reached
            # thus it no longer uses .wait_for_temp()
        protocol.pause('Load competent cells, uncap and resume run')

        # Transfer final assemblies
        p20_pipette.transfer(ASSEMBLY_VOL,
                             [assembly_plate.wells_by_name()[well_name] for well_name in transformation_wells],
                             [transformation_plate.wells_by_name()[well_name] for well_name in transformation_wells],
                             new_tip='always',
                             mix_after=(MIX_SETTINGS))


        # Incubate for 20 minutes and remove competent cells for heat shock
        protocol.delay(minutes=INCUBATION_TIME)


        protocol.pause('Remove transformation reactions, conduct heatshock and replace.')


    def phase_switch():
        """
        Function pauses run enabling addition/removal of labware.

        """
        protocol.pause('Remove final assembly plate. Introduce agar tray and deep well plate containing SOC media. Resume run.')

    def outgrowth(
            cols,
            soc_well):
        """
        Outgrows transformed cells.

        Args:
        cols (list of str): list of cols in transformation plate containing samples.
        soc_well (str): Well containing SOC media in relevant plate.

        """

        # Constants
        SOC_VOL = 125
        SOC_MIX_SETTINGS = (4, 50)
        TEMP = 37
        OUTGROWTH_TIME = 60
        SOC_ASPIRATION_RATE = 25
        P300_DEFAULT_ASPIRATION_RATE = 150

        # Define wells
        transformation_cols = [transformation_plate.columns_by_name()[column] for column in cols]

        soc = soc_plate.wells(soc_well)

        # Add SOC to transformed cells
        p300_pipette.flow_rate.aspirate = SOC_ASPIRATION_RATE
        p300_pipette.transfer(SOC_VOL, soc, transformation_cols,
                              new_tip='always', mix_after=SOC_MIX_SETTINGS)
        p300_pipette.flow_rate.aspirate = P300_DEFAULT_ASPIRATION_RATE

        # Incubate for 1 hour at 37 °C
        tempdeck.set_temperature(TEMP)

        protocol.delay(minutes=OUTGROWTH_TIME)


        tempdeck.deactivate()


    def spotting_cols(spotting_tuples):
        """
        Evaluates spotting_tuples and returns unique cols (str) associated with each spotting_tuple's source wells.

        Args:
        spotting_tuples (list): Sets of spotting reactions are given in the form: ((source wells), (target wells), (spotting volumes)).

        """
        cols_list = []
        for spotting_tuple in spotting_tuples:
            source_wells_cols = [source_well[1:] for source_well in spotting_tuple[0]]
            unique_cols = [col for i, col in enumerate(source_wells_cols) if source_wells_cols.index(col) == i]
            cols_list.append(unique_cols)
        return cols_list


    def spot_transformations(
            spotting_tuples,
            dead_vol=1,
            spotting_dispense_rate=0.025,
            stabbing_depth=10,
            max_spot_vol=5):
        """
        Spots transformation reactions.

        Args:
        spotting_tuples (list): Sets of spotting reactions are given in the form: ((source wells), (target wells), (spotting volumes)).
        dead_vol (float): Dead volume aspirated during spotting.
        spotting_dispense_rate (float): Rate p20_pipette dispenses at during spotting.
        stabbing_depth (float): Depth p20_pipette moves into agar during spotting.
        max_spot_vol (float): Maximum volume that is spotted per spot reaction.

        """

        def spot(
                source,
                target,
                spot_vol):
            """
            Spots an individual reaction using the p20 pipette.

            Args:
            source (str): Well containing the transformation reaction to be spotted.
            target (str): Well transformation reaction is to be spotted to.
            spot_vol (float): Volume of transformation reaction to be spotted (uL).

            """

            # Constants
            DEFAULT_HEAD_SPEED = {'x': 400, 'y': 400,'z': 125, 'a': 125}
            SPOT_HEAD_SPEED = {'x': 400, 'y': 400, 'z': 125,'a': 125 // 4}
            DISPENSING_HEIGHT = 5
            SAFE_HEIGHT = 7  # height avoids collision with agar tray.

            # Spot
            p20_pipette.pick_up_tip()
            p20_pipette.aspirate(spot_vol + dead_vol, source[0])
            # old code:
                # p20_pipette.aspirate(spot_vol + dead_vol, source)
                # returned type error because 'source' was a list containing one item (the well location)
                # source[0] takes the location out of the list

            p20_pipette.move_to(target[0].top(SAFE_HEIGHT))
            p20_pipette.move_to(target[0].top(DISPENSING_HEIGHT))
            # old code:
                # p20_pipette.move_to(target.top(SAFE_HEIGHT))
                # p20_pipette.move_to(target.top(DISPENSING_HEIGHT))
                # returned attribute error because 'target' was a list containing one item (the well location)
                # target[0] takes the location out of the list

            p20_pipette.dispense(volume=spot_vol, rate=spotting_dispense_rate)

            protocol.max_speeds.update(SPOT_HEAD_SPEED)
            # old code:
                # robot.head_speed(combined_speed=max(SPOT_HEAD_SPEED.values()), **SPOT_HEAD_SPEED)
                # robot.head_speed not used in API version 2
                # replaced with protocol.max_speeds
            # new code no longer uses the lower value between combined speed or specified speed
                # just uses each axis' specified speed directly
            p20_pipette.move_to(target[0].top(-1 * stabbing_depth))
            # old code:
                # p20_pipette.move_to(target.top(-1*stabbing_depth))
                # returns attribute error because 'target' was a list containing one item (the well location)
            protocol.max_speeds.update(DEFAULT_HEAD_SPEED)
            # old code:
                # robot.head_speed(combined_speed=max(DEFAULT_HEAD_SPEED.values()), **DEFAULT_HEAD_SPEED)
                # robot.head_speed not used in API version 2
                # replaced with protocol.max_speeds
            # new code no longer uses the lower value between combined speed or specified speed
                # just uses each axis' specified speed directly
            p20_pipette.move_to(target[0].top(SAFE_HEIGHT))
            # old code:
                # p20_pipette.move_to(target[0].top(SAFE_HEIGHT))
                # returns attribute error because 'target' was a list containing one item (the well location)


            # the code below makes sure that the transformend cells are efficiently reaching to the agar surface

            p20_pipette.blow_out()

            protocol.delay(seconds=10)

            p20_pipette.blow_out()

            protocol.delay(seconds=10)

            # Dispose of dead volume and tip
            p20_pipette.dispense(dead_vol, spotting_waste[0])

            p20_pipette.blow_out()
                # the simple .blow_out command blows out at current position (spotting waste) by defualt
                # unlike blowout=true in complex commands, which by default will blow out in waste

            p20_pipette.drop_tip()

        def spot_tuple(spotting_tuple):
            """
            Spots all reactions defined by the spotting tuple. Requires the function spot.

            Args:
            spotting_tuple (tuple): Spotting reactions given in the form: (source wells), (target wells), (spotting volumes).
            Each unique source well is resuspended once prior to spotting.

            """
            source_wells = spotting_tuple[0]
            target_wells = spotting_tuple[1]
            spot_vols = list(spotting_tuple[2])
            while max(spot_vols) > 0:
                for index, spot_vol in enumerate(spot_vols):
                    if spot_vol == 0:
                        pass
                    else:
                        vol = spot_vol if spot_vol <= max_spot_vol else max_spot_vol
                        spot(source = transformation_plate.wells(source_wells[index]), target = agar_plate.wells(target_wells[index]), spot_vol = vol)
                        spot_vols[index] = spot_vols[index] - vol

        # Constants
        TRANSFORMATION_MIX_SETTINGS = [4, 50]

        # Spot transformation reactions
            # Each unique transformation well is resuspended once prior to spotting.

        for spotting_tuple in spotting_tuples:
            source_wells_cols = [source_well[1:] for source_well in spotting_tuple[0]]
            unique_cols = [col for i, col in enumerate(source_wells_cols) if source_wells_cols.index(col) == i]
            for col in unique_cols:
                p300_pipette.pick_up_tip()
                p300_pipette.mix(TRANSFORMATION_MIX_SETTINGS[0], TRANSFORMATION_MIX_SETTINGS[1],transformation_plate.columns_by_name()[col][0])
                p300_pipette.drop_tip()
            spot_tuple(spotting_tuple)

     #Tiprack slots
    p20_p300_tiprack_slots = tiprack_slots(spotting_tuples)
    p20_slots = CANDIDATE_p20_SLOTS[:p20_p300_tiprack_slots[0]]
    p300_slots = CANDIDATE_P300_SLOTS[:p20_p300_tiprack_slots[1]]
    # Define labware
    p20_tipracks = [protocol.load_labware(p20_TIPRACK_TYPE, slot) for slot in p20_slots]
        # changed to protocol.load_labware for API version 2
    p300_tipracks = [protocol.load_labware(P300_TIPRACK_TYPE, slot) for slot in p300_slots]
        # changed to protocol.load_labware for API version 2
    p20_pipette = protocol.load_instrument(__LABWARES['p10_single']['id'], P20_MOUNT, tip_racks=p20_tipracks)
        # changed to protocol.load_instrument for API version 2
    p300_pipette = protocol.load_instrument(__LABWARES['p300_multi']['id'], P300_MOUNT, tip_racks=p300_tipracks)
        # changed to protocol.load_instrument for API version 2
    assembly_plate = protocol.load_labware(ASSEMBLY_PLATE_TYPE, ASSEMBLY_PLATE_SLOT)
        # changed to protocol.load_labware for API version 2
    tempdeck = protocol.load_module('tempdeck', TEMPDECK_SLOT)
    transformation_plate = tempdeck.load_labware(TRANSFORMATION_PLATE_TYPE, TEMPDECK_SLOT)
        # changed to protocol.load_labware for API version 2
        # removed share=True, not required in API version 2
        # removed TEMPDECK_SLOT as it is loaded directly onto temperature module
    soc_plate = protocol.load_labware(SOC_PLATE_TYPE, SOC_PLATE_SLOT)
        # changed to protocol.load_labware for API version 2
    tube_rack = protocol.load_labware(TUBE_RACK_TYPE, TUBE_RACK_SLOT)
        # changed to protocol.load_labware for API version 2
    spotting_waste = tube_rack.wells(SPOTTING_WASTE_WELL)
    agar_plate = protocol.load_labware(AGAR_PLATE_TYPE, AGAR_PLATE_SLOT)
        # changed to protocol.load_labware for API version 2
    
    ### Run protocol


    # Register agar_plate for calibration
    p20_pipette.transfer(1, agar_plate.wells('A1'), agar_plate.wells('H12'), trash=False)
    # removed:
        # p20_pipette.start_at_tip(p20_tipracks[0][0])
        # pipette automatically starts from 'A1' tiprack location
        # if re-adding, need to use p20.pipette.starting_tip() instead of p20.pipette.start_at_tip()


    # Run functions
    # Run functions
    transformation_setup(generate_transformation_wells(spotting_tuples))
    phase_switch()
    spotting_tuples_cols = [col for cols in spotting_cols(spotting_tuples) for col in cols]
    unique_cols = [col for i, col in enumerate(spotting_tuples_cols) if spotting_tuples_cols.index(col) == i]
    outgrowth(cols=unique_cols, soc_well=soc_well)
    spot_transformations(spotting_tuples)
    # Spot again to increase the chances of getting more colonies. Second spotting will only work for small number of assemblies where there is enough space on the deck for tipracks.
    # protocol.pause('Let the spotted cells get dry')
    # spot_transformations(spotting_tuples)
    print(unique_cols)
