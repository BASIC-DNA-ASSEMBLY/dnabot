import opentrons.simulate
#attempts to get the simulate to run with custom labware - does not work
#protocol_file = open('c:/users/geoff/github/DNA-BOT/dnabot/template_ot2_scripts/clip_template_Thermocycler_Gen2_APIv2_19.py')
protocol_file = open('c:/users/geoff/github/DNA-BOT/dnabot/template_opentrons_scripts/1_FLEX_clip_template_APIv2_21.py')
#C:\Users\Geoff\GitHub\DNA-BOT\dnabot\MRes2024\1_MRes_clip_Thermocycler_Gen2_APIv2_19.py
#opentrons.simulate.simulate(protocol_file) -L --custom-labware-path 'C:/users/geoff/github/DNA-BOT/labware/Custom_labware'
#opentrons.simulate.simulate(protocol_file) -L, -custom-labware-path=='C:/users/geoff/github/DNA-BOT/labware/Custom_labware'

#protocol_file = open('c:/users/geoff/github/DNA-BOT/dnabot/template_ot2_scripts/simple_protocol_test.py')
opentrons.simulate.simulate(protocol_file) 
#opentrons.simulate.simulate(protocol_file) -L, -custom-labware-path=='C:/users/geoff/github/DNA-BOT/labware/Custom_labware'

