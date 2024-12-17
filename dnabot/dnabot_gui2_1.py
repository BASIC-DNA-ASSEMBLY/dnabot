# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:35:26 2019

@author: mh2210, tduigou
"""

from __future__ import annotations  # Enable the "hint" feature for objects

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def to_numeric_value(str_value: str):
    if float(str_value).is_integer():
        return int(float(str_value))
    else:
        return float(str_value)


class FileSelector:

    def __init__(self, root, irow, title, multiple_files=False):
        # To be used to get the value from outside
        self.output = None
        self.irow = irow
        # Settings
        self.title = title
        self.multiple_files = multiple_files
        # File path as text
        self.entry_text = tk.Entry(root, state="readonly", width=60)
        self.entry_text.insert(0, '')
        # Browse button
        button = tk.Button(root, text='Browse', command=self.browse_file)
        # Position on grid
        button.grid(row=self.irow, columnspan=2)
        self.irow += 1
        self.entry_text.grid(row=self.irow, columnspan=2)
        self.irow += 1

    def browse_file(self):
        if self.multiple_files:
            output = filedialog.askopenfilenames(  # output is a list
                title=self.title,
                filetypes=(('CSV files', '*.csv'), ('All files', '*.*'))
                )
        else:
            # Output is a str
            output = filedialog.askopenfilename(  # output is a str
                title=self.title,
                filetypes=(('CSV files', '*.csv'), ('All files', '*.*'))
                )
        self.output = output
        self.update_text()
    
    def update_text(self):
        self.entry_text.configure(state='normal')
        self.entry_text.delete(0, "end")
        if isinstance(self.output, tuple):
            self.entry_text.insert(0, ', '.join(self.output))
        else:
            self.entry_text.insert(0, self.output)
        self.entry_text.configure(state='readonly')

    def get(self):
        return self.output


class GUI:

    __APP_TITLE = "DNABot App"
    __APP_FONT = ("Helvetica", 12)
    __TROUGH_WELLS = ['A{}'.format(x + 1) for x in range(12)]

    
    def __init__(
        self,
        root: tk.Tk,
        user_settings = dict
        ) -> GUI:
    
        # The set up the GUI backbone
        self.root = root
        self.canvas = tk.Canvas(self.root, width=900, height=820)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview, width=25)
        self.vsb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.pack(side="left", fill="both", expand=False)
        self.canvas.create_window((10,0), window=self.frame, anchor="nw", tags="self.frame")

        # 
        self.root.title(GUI.__APP_TITLE)
        self.user_settings = user_settings
        self.quit_status = False

        # Intro ===============================================================
        irow = 0
        intro = tk.Message(
            self.frame,
            text=(
                "Welcome to the dnabot App v2.0! Please follow these "
                "instructions to create the 4 DNA-BOT scripts:"),
            width=850, font=('Arial', 18, 'bold'))
        intro.grid(row=irow, columnspan=2, padx=5, pady=15)

        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Robot Type  =================================================

        irow += 1
        message_1 = tk.Message(
            self.frame,
            text=(
                "1 - From the dropdown menus select the robot that you are using: OT2 or FLEX "
                ),
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_1.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        irow += 1
        robot_type_label = tk.Label(self.frame, text='Robot Type', font=('Arial', 12, 'bold'))
        robot_type_label.grid(row=irow, column=0, sticky='e')
        self.robot_type = tk.StringVar(self.frame)
        self.robot_type.set("OT2")
        Robot_choice= ["OT2","FLEX"]
        Robot_type_x=tk.OptionMenu(self.frame, self.robot_type, 'OT2')
        Robot_type_x=tk.OptionMenu(self.frame, self.robot_type, *Robot_choice)
        Robot_type_x.grid(row=irow, column=1, sticky=tk.W)
        Robot_type_x.config(font=GUI.__APP_FONT)

        irow += 1
        self.__add_separator(irow)
        irow += 1
       ############################################################################
       ############################################################################
        # Hardware  =================================================
        irow += 1
        message_1 = tk.Message(
            self.frame,
            text=(
                "2 - From the dropdown menus select the hardware that you are using."
                 ),
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_1.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        irow += 1
        single_pipette_label = tk.Label(self.frame, text='Single Pipette: OT2 P20 or FLEX P50 Pipette', font=('Arial', 12))
        single_pipette_label.grid(row=irow, column=0, sticky='e')
        self.single_pipette = tk.StringVar(self.frame)
        self.single_pipette.set("p20_single_gen2")
        single_pipette_choice= ["p20_single_gen2","flex_1channel_50"]
        single_pipette_x=tk.OptionMenu(self.frame, self.single_pipette, *single_pipette_choice)
        single_pipette_x.grid(row=irow, column=1, sticky=tk.W)
        single_pipette_x.config(font=GUI.__APP_FONT)
        irow += 1
        single_pipette_mount_label = tk.Label(self.frame, text='Single Pipette Mount', font=('Arial', 12))
        single_pipette_mount_label.grid(row=irow, column=0, sticky='e')
        self.single_pipette_mount = tk.StringVar(self.frame)
        self.single_pipette_mount.set("right")
        single_pipette_mount_choice= ["left","right"]
        single_pipette_mount_x=tk.OptionMenu(self.frame, self.single_pipette_mount, *single_pipette_mount_choice)
        single_pipette_mount_x.grid(row=irow, column=1, sticky=tk.W)
        single_pipette_mount_x.config(font=GUI.__APP_FONT)

        irow += 1
        multi_pipette_label = tk.Label(self.frame, text='Multi-channel Pipette: OT2 P300 or FLEX P1000 8-channel Pipette', font=('Arial', 12))
        multi_pipette_label.grid(row=irow, column=0, sticky='e')
        self.multi_pipette = tk.StringVar(self.frame)
        self.multi_pipette.set("p300_multi_gen2")
        multi_pipette_choice= ["p300_multi_gen2","flex_8channel_1000"]
        multi_pipette_x=tk.OptionMenu(self.frame, self.multi_pipette, *multi_pipette_choice)
        multi_pipette_x.grid(row=irow, column=1, sticky=tk.W)
        multi_pipette_x.config(font=GUI.__APP_FONT)
        irow += 1
        multi_pipette_mount_label = tk.Label(self.frame, text='Multi Pipette Mount', font=('Arial', 12))
        multi_pipette_mount_label.grid(row=irow, column=0, sticky='e')
        self.multi_pipette_mount = tk.StringVar(self.frame)
        self.multi_pipette_mount.set("left")
        multi_pipette_mount_choice= ["left","right"]
        multi_pipette_mount_x=tk.OptionMenu(self.frame, self.multi_pipette_mount, *multi_pipette_mount_choice)
        multi_pipette_mount_x.grid(row=irow, column=1, sticky=tk.W)
        multi_pipette_mount_x.config(font=GUI.__APP_FONT)

        irow += 1
        thermocycler_label = tk.Label(self.frame, text='Thermocylcer Module: Gen1 or Gen2', font=('Arial', 12,))
        thermocycler_label.grid(row=irow, column=0, sticky='e')
        self.thermocycler = tk.StringVar(self.frame)
        self.thermocycler.set("thermocyclerModuleV2")
        thermocycler_choice= ["thermocyclerModuleV2","thermocyclerModuleV1"]
        thermocycler_x=tk.OptionMenu(self.frame, self.thermocycler, *thermocycler_choice)
        thermocycler_x.grid(row=irow, column=1, sticky=tk.W)
        thermocycler_x.config(font=GUI.__APP_FONT)

        irow += 1
        mag_deck_label = tk.Label(self.frame, text='OT2 Magnetic Module or Flex Block', font=('Arial', 12,))
        mag_deck_label.grid(row=irow, column=0, sticky='e')
        self.mag_deck = tk.StringVar(self.frame)
        self.mag_deck.set("magnetic module gen1")
        mag_deck_choice= ["magnetic module gen1","magnetic module gen2", "magneticBlockV1"]
        mag_deck_x=tk.OptionMenu(self.frame, self.mag_deck, *mag_deck_choice)
        mag_deck_x.grid(row=irow, column=1, sticky=tk.W)
        mag_deck_x.config(font=GUI.__APP_FONT)

        irow += 1
        self.__add_separator(irow)
        irow += 1

        # Labware IDs =========================================================
        irow += 1
        message_2 = tk.Message(
            self.frame,
            text=(
                "3 - Specify the labware IDs to be used. \nDefault choices are shown, leave as is to use these."),
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_2.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        # Opentrons 4-in-1 tubes rack for 1.5 ml eppendorf tubes
        irow += 1
        self.labware_24_tuberack_1500ul_entry = self.__make_labware_entry(
            label="Opentrons 4-in-1 tubes rack",
            labware_id='24_tuberack_1500ul',
            irow=irow)
        # Opentrons 10μL tips rack
        irow += 1
        self.labware_96_tiprack_20ul_entry = self.__make_labware_entry(
            label="Opentrons 20μL tips rack",
            labware_id='96_tiprack_20ul',
            irow=irow)
        # Opentrons 300μL tips rack
        irow += 1
        self.labware_96_tiprack_300ul_entry = self.__make_labware_entry(
            label="Opentrons 300μL tips rack",
            labware_id='96_tiprack_300ul',
            irow=irow)
        # Clip reaction source plate (steps: clip)
        irow += 1
        self.labware_clip_source_plate_entry = self.__make_labware_entry(
            label="Clip reaction source plate (steps: clip)",
            labware_id='clip_source_plate',
            irow=irow)
        # Clip reaction plate (steps: clip, purif, assembly)
        irow += 1
        self.labware_clip_plate_entry = self.__make_labware_entry(
            label="Clip reaction plate (steps: clip, purification, assembly)",
            labware_id='clip_plate',
            irow=irow)
        # Mix plate (step: purification)
        irow += 1
        self.labware_mix_plate_entry = self.__make_labware_entry(
            label="Mix plate (step purification)",
            labware_id='mix_plate',
            irow=irow)
        # Final assembly plate (steps: assembly, transformation)
        irow += 1
        self.labware_final_assembly_plate_entry = self.__make_labware_entry(
            label="Final assembly plate (steps: assembly, transformation)",
            labware_id='final_assembly_plate',
            irow=irow)
        # Transformation plate (step: transformation)
        irow += 1
        self.labware_transform_plate_entry = self.__make_labware_entry(
            label="Transformation plate (step: transformation)",
            labware_id='transform_plate',
            irow=irow)
        # Transformation plate without thermocycler (step: transformation)
        irow += 1
        self.labware_transform_plate_wo_thermo_entry = self.__make_labware_entry(
            label="Transformation plate without thermocycler (step: transformation)",
            labware_id='transform_plate_wo_thermo',
            irow=irow)
        # Agar plate (transformation step)
        irow += 1
        self.agar_plate_entry = self.__make_labware_entry(
            label="Agar plate (transformation step)",
            labware_id='agar_plate',
            irow=irow)
        # Reservoir plate 21 mL 12 channels
        irow += 1
        self.labware_12_reservoir_21000ul_entry = self.__make_labware_entry(
            label="Reservoir plate 21 mL 12 channels",
            labware_id='12_reservoir_21000ul',
            irow=irow)
        # 96 deep well plate 2 mL wells
        irow += 1
        self.labware_96_deepwellplate_2ml_entry = self.__make_labware_entry(
            label="96 deep well plate 2 mL wells",
            labware_id='96_deepwellplate_2ml',
            irow=irow)
        # Corning 12 Well Plate 6.9 mL Flat
        irow += 1
        self.labware_12_corning_wellplate_entry = self.__make_labware_entry(
            label="Corning 12 Well Plate 6.9 mL Flat",
            labware_id="12_corning_wellplate",
            irow=irow)
        
        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Ethanol & SOC media =================================================
        irow += 1
        message_1 = tk.Message(
            self.frame,
            text=(
                "4 - From the dropdown menus select wells/columns for \n"
                "  a.) Ethanol (for the purification - script 2) \n  b.) SOC media "
                "(for the transformation - script-4)."),
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_1.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        irow += 1
        etoh_well_label = tk.Label(self.frame, text='a.) Trough well for ethanol during purification:', font=('Arial', 12))
        etoh_well_label.grid(row=irow, column=0, sticky='e')
        self.etoh_well = tk.StringVar(self.frame)
        self.etoh_well.set(GUI.__TROUGH_WELLS[10])
        etoh_w=tk.OptionMenu(self.frame, self.etoh_well, *tuple(GUI.__TROUGH_WELLS[1:11]))
        etoh_w.grid(row=irow, column=1, sticky=tk.W)
        etoh_w.config(font=GUI.__APP_FONT)
        
        irow += 1
        soc_column_label = tk.Label(self.frame, text='b.) Deep-well plate column for SOC media during transformation:', font=('Arial', 12))
        soc_column_label.grid(row=irow, column=0, sticky='e')
        self.soc_column=tk.StringVar(self.frame)
        self.soc_column.set("1")
        soc_w=tk.OptionMenu(self.frame, self.soc_column, *tuple(['{}'.format(x + 1) for x in range(12)]))
        soc_w.grid(row=irow, column=1, sticky='w')
        soc_w.config(font=GUI.__APP_FONT)

        irow += 1
        self.__add_separator(irow)

        # Parameters for the clip reaction step ===============================
        irow += 1
        message_3 = tk.Message(
            self.frame,
            text="5 - Specify parameters for the clip reaction step.",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_3.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        irow += 1
        premix_linkers_label = tk.Label(self.frame, text='Premix the linker plate (Yes or No)?', font=('Arial', 12))
        premix_linkers_label.grid(row=irow, column=0, sticky='e')
        self.param_premix_linkers = tk.StringVar(self.frame)
        self.param_premix_linkers.set('Yes')
        boolean = ['Yes','No']
        premix_l=tk.OptionMenu(self.frame, self.param_premix_linkers, *boolean)
        premix_l.grid(row=irow, column=1, sticky=tk.W)
        premix_l.config(font=GUI.__APP_FONT)

        irow += 1
        premix_parts_label = tk.Label(self.frame, text='Premix the part plate (Yes or No)?', font=('Arial', 12))
        premix_parts_label.grid(row=irow, column=0, sticky='e')
        self.param_premix_parts = tk.StringVar(self.frame)
        self.param_premix_parts.set('Yes')
        boolean = ['Yes','No']
        premix_p=tk.OptionMenu(self.frame, self.param_premix_parts, *boolean)
        premix_p.grid(row=irow, column=1, sticky=tk.W)
        premix_p.config(font=GUI.__APP_FONT)
        

        #=================================================================
        # =================================================================
        irow += 1
        message_3b = tk.Message(
            self.frame,text="Minimum part and linker volumes in your plates."
            "\nYou are advised that the recommended dead (unused) volume is 15 ul,"
            "\nplus you should have sufficient to account for usage and "
            "\nevaporation at a rate of 1 ul/hour."
            "\n          These volumes will be used to adjust the pre-mix volume if used:",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_3b.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')
        
        irow += 1
        self.param_linkers_volume = self.__make_parameter_entry(
            label="min. volume of linkers (ul)",
            parameter_id="linkers_volume",
            irow=irow)
        
        irow += 1
        self.param_parts_volume = self.__make_parameter_entry(
             label="min. volume of parts (ul)",
             parameter_id="parts_volume",
             irow=irow)

        irow += 1
        message_3c = tk.Message(
            self.frame,
            text="Thermocycler settings:",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_3c.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')       
        
        irow += 1
        self.param_thermo_temp = self.__make_parameter_entry(
             label="Temp of thermocycler block during setup",
             parameter_id="thermo_temp",
             irow=irow)     
        irow += 1
        clip_keep_thermo_lid_closed_label = tk.Label(self.frame, text='Keep the thermocycler lid closed at 4°C at the end of execution (Yes or No)?', font=('Arial', 12))
        clip_keep_thermo_lid_closed_label.grid(row=irow, column=0, sticky='e')
        self.param_clip_keep_thermo_lid_closed = tk.StringVar(self.frame)
        self.param_clip_keep_thermo_lid_closed.set('No')
        boolean = ['Yes','No']
        thermo_l=tk.OptionMenu(self.frame, self.param_clip_keep_thermo_lid_closed, *boolean)
        thermo_l.grid(row=irow, column=1, sticky=tk.W)
        thermo_l.config(font=GUI.__APP_FONT)
        
  
    
        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Parameters for the purification step ================================
        irow += 1
        message_4 = tk.Message(
            self.frame,
            text="6 - Specify parameters for the purification step.",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_4.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')       
        
        irow += 1
        message_1 = tk.Message(
            self.frame,
            text=(
                "Select parameters for the magnetic module (if used) and purification"
                ),
            width=850,
            anchor='w',
            font=('Arial', 12,))
        message_1.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')

        irow += 1
        self.param_purif_magdeck_height = self.__make_parameter_entry(
            label="Height to raise magnets in magnetic module (mm) \n (ignore for Flex magnetic block)",
            parameter_id="purif_magdeck_height",
            irow=irow)
        irow += 1
        self.param_purif_wash_time = self.__make_parameter_entry(
            label="Mag bead washing time (min)",
            parameter_id="purif_wash_time",
            irow=irow)
        irow += 1
        self.param_purif_bead_ratio = self.__make_parameter_entry(
            label="Mag bead ratio",
            parameter_id="purif_bead_ratio",
            irow=irow)
        irow += 1
        self.param_purif_incubation_time = self.__make_parameter_entry(
            label="Mag bead incubation time (min)",
            parameter_id="purif_incubation_time",
            irow=irow)
        irow += 1
        self.param_purif_settling_time = self.__make_parameter_entry(
            label="Mag bead settling time (min)",
            parameter_id="purif_settling_time",
            irow=irow)
        irow += 1
        self.param_purif_drying_time = self.__make_parameter_entry(
            label="Mag bead drying time (min)",
            parameter_id="purif_drying_time",
            irow=irow)
        irow += 1
        self.param_purif_elution_time = self.__make_parameter_entry(
            label="Elution time (min)",
            parameter_id="purif_elution_time",
            irow=irow)

        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Parameters for the transformation step ==============================
        irow += 1
        message_5 = tk.Message(
            self.frame,
            text="7 - Specify parameters for the transformation step.",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_5.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')
        irow += 1
        self.param_transform_incubation_temp = self.__make_parameter_entry(
            label="Incubation temperature (°C)",
            parameter_id="transform_incubation_temp",
            irow=irow)
        irow += 1
        self.param_transform_incubation_time = self.__make_parameter_entry(
            label="Incubation time (min)",
            parameter_id="transform_incubation_time",
            irow=irow)

        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Construct CSV file ==================================================
        irow += 1
        message_6 = tk.Message(
            self.frame,
            text="8 - Select the CSV file describing constructs.",
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_6.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')
        irow += 1
        self.construct_file_selector = FileSelector(self.frame, irow, title='Construct CSV file', multiple_files=False)
        irow = self.construct_file_selector.irow

        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # Source CSV files ====================================================
        irow += 1
        message_7 = tk.Message(
            self.frame,
            text=(
                "9 - Select up to 6 csv files describing plates "
                "containing BASIC parts and linkers. If all files "
                "are not within one folder, absolute paths should "
                "be given."),
            width=850,
            anchor='w',
            font=('Arial', 12, 'bold'))
        message_7.grid(row=irow, columnspan=2, padx=5, pady=10, sticky='w')
        irow += 1
        self.source_files_selector = FileSelector(self.frame, irow, title='Source CSV files', multiple_files=True)
        irow = self.source_files_selector.irow

        # Sep =================================================================
        irow += 1
        self.__add_separator(irow)

        # # White space
        # irow += 1
        # spacer = tk.Label(self.frame, text="", font=GUI.__APP_FONT)
        # spacer.grid(row=irow, columnspan=2, padx=5, pady=10)

        # Quit and generate buttons
        irow += 1
        quit_button = tk.Button(self.frame, text='QUIT', fg='red', command=self.quit, font=GUI.__APP_FONT)
        quit_button.grid(row=irow, column=0, pady=10)
        generate_button=tk.Button(self.frame, text='GENERATE', command=self.generate, font=GUI.__APP_FONT)
        generate_button.grid(row=irow, column=1, pady=10)

        # Upate scroll region info
        self.root.update()  # Required to refresh canvas scrollreion
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

        # 
        self.frame.mainloop()


    def quit(self):
        self.quit_status=True
        self.root.quit()

    def generate(self):
        # Step 1        
        self.user_settings['robot_type'] = self.robot_type.get()

        # Hardware IDs
        self.user_settings['hardware']['single_pipette']['id'] = self.hardware_single_pipette.get()
        self.user_settings['hardware']['single_pipette_mount']['id'] = self.hardware_single_pipette_mount.get()
        self.user_settings['hardware']['multi_pipette']['id'] = self.hardware_multi_pipette.get()
        self.user_settings['hardware']['multi_pipette_mount']['id'] = self.hardware_multi_pipette_mount.get()
        self.user_settings['hardware']['thermocycler']['id'] = self.hardware_thermocycler.get()
        self.user_settings['hardware']['mag_deck']['id'] = self.hardware_mag_deck_entry.get()
        #self.user_settings['hardware']['mag_deck_options_list']['list'] = self.labware_mag_deck_entry.get()
        
        # Labware IDs
        self.user_settings['labwares']['24_tuberack_1500ul']['id'] = self.labware_24_tuberack_1500ul_entry.get()
        self.user_settings['labwares']['96_tiprack_20ul']['id'] = self.labware_96_tiprack_20ul_entry.get()
        self.user_settings['labwares']['96_tiprack_300ul']['id'] = self.labware_96_tiprack_300ul_entry.get()
        self.user_settings['labwares']['clip_source_plate']['id'] = self.labware_clip_source_plate_entry.get()
        self.user_settings['labwares']['clip_plate']['id'] = self.labware_clip_plate_entry.get()
        self.user_settings['labwares']['mix_plate']['id'] = self.labware_mix_plate_entry.get()
        self.user_settings['labwares']['final_assembly_plate']['id'] = self.labware_final_assembly_plate_entry.get()
        self.user_settings['labwares']['transform_plate']['id'] = self.labware_transform_plate_entry.get()
        #remove transformation protocol without thermocycler
        #self.user_settings['labwares']['transform_plate_wo_thermo']['id'] = self.labware_transform_plate_wo_thermo_entry.get()
        self.user_settings['labwares']['agar_plate']['id'] = self.agar_plate_entry.get()
        self.user_settings['labwares']['12_reservoir_21000ul']['id'] = self.labware_12_reservoir_21000ul_entry.get()
        self.user_settings['labwares']['96_deepwellplate_2ml']['id'] = self.labware_96_deepwellplate_2ml_entry.get()
        self.user_settings['labwares']['12_corning_wellplate']['id'] = self.labware_12_corning_wellplate_entry.get()
        #EtOH and SOC
        self.user_settings['etoh_well'] = self.etoh_well.get()
        self.user_settings['soc_column'] = self.soc_column.get()
        # Parameters for the clip reaction step        
        self.user_settings["parameters"]["premix_linkers"]["id"] = self.param_premix_linkers.get()
        self.user_settings["parameters"]["premix_parts"]["id"] = self.param_premix_parts.get()
        self.user_settings['parameters']['linkers_volume']['value'] = to_numeric_value(self.param_linkers_volume.get())
        self.user_settings['parameters']['parts_volume']['value'] = to_numeric_value(self.param_parts_volume.get())
        self.user_settings["parameters"]["clip_keep_thermo_lid_closed"]["id"] = self.param_clip_keep_thermo_lid_closed.get()
        self.user_settings['parameters']['thermo_temp']['value'] = to_numeric_value(self.param_thermo_temp.get())      
        # Parameters for the purification step
        self.user_settings['parameters']['purif_magdeck_height']['value'] = to_numeric_value(self.param_purif_magdeck_height.get())
        self.user_settings['parameters']['purif_wash_time']['value'] = to_numeric_value(self.param_purif_wash_time.get())
        self.user_settings['parameters']['purif_bead_ratio']['value'] = to_numeric_value(self.param_purif_bead_ratio.get())
        self.user_settings['parameters']['purif_incubation_time']['value'] = to_numeric_value(self.param_purif_incubation_time.get())
        self.user_settings['parameters']['purif_settling_time']['value'] = to_numeric_value(self.param_purif_settling_time.get())
        self.user_settings['parameters']['purif_drying_time']['value'] = to_numeric_value(self.param_purif_drying_time.get())
        self.user_settings['parameters']['purif_elution_time']['value'] = to_numeric_value(self.param_purif_elution_time.get())
        # Parameters for the transformation step
        self.user_settings['parameters']['transform_incubation_temp']['value'] = to_numeric_value(self.param_transform_incubation_temp.get())
        self.user_settings['parameters']['transform_incubation_time']['value'] = to_numeric_value(self.param_transform_incubation_time.get())
        # Construct CSV file
        self.user_settings['construct_path'] = self.construct_file_selector.get()
        # Source CSV files
        self.user_settings['sources_paths'] = self.source_files_selector.get()
        self.root.quit()

    def __make_labware_entry(self, label, labware_id, irow):
        labware_label = tk.Label(self.frame, text=label, font=GUI.__APP_FONT)
        labware_label.grid(row=irow, column=0, sticky='e')
        labware_entry = tk.Entry(self.frame, width=40)
        labware_entry.insert(0, self.user_settings["labwares"][labware_id]['id'])
        labware_entry.grid(row=irow, column=1, sticky='w')
        return labware_entry

    def __make_parameter_entry(self, label, parameter_id, irow, parameter_value="value"):
        parameter_label = tk.Label(self.frame, text=label, font=GUI.__APP_FONT)
        parameter_label.grid(row=irow, column=0, sticky='e')
        parameter_entry = tk.Entry(self.frame, width=20)
        parameter_entry.insert(0, self.user_settings["parameters"][parameter_id][parameter_value])
        parameter_entry.grid(row=irow, column=1, sticky='w')
        return parameter_entry

    def __add_separator(self, irow):
        ttk.Separator(
            self.frame,
            orient=tk.HORIZONTAL
        ).grid(
            row=irow,
            columnspan=2,
            sticky="ew"
        )