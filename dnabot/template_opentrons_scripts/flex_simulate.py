from opentrons.simulate import get_protocol_api as original_get_protocol_api
from opentrons.simulate import simulate as original_simulate
from opentrons.protocol_api import ProtocolContext
from typing import Union, Dict, Optional
from opentrons.protocols.api_support.types import APIVersion
from opentrons.hardware_control import ThreadManagedHardware
from opentrons_shared_data.labware.labware_definition import LabwareDefinition
"""
Add the follwoing snippet to the end of the protocol to allow debugging of the flex. 
if __name__ == "__main__":
    #robot_type = input("Enter robot type (Flex or OT-2): ").strip() or "Flex"
    robot_type = "Flex"
    from flex_simulate import FlexibleSimulate
    # Use the custom FlexSimulate class
    protocol = FlexibleSimulate.get_protocol_api("2.19", robot_type=robot_type)  # Ensure the correct API level is used

    # Debugging: inspect protocol setup
    print(f"Simulated robot type: {protocol.robot_type}")
    run(protocol)  # Call the `run` function for the protocol logic
"""

class FlexibleSimulate:
    """
    A custom simulation class that allows dynamic selection of the robot type
    (e.g., Flex or OT-2).
    """

    @staticmethod
    def get_protocol_api(
        version: Union[str, APIVersion],
        bundled_labware: Optional[Dict[str, LabwareDefinition]] = None,
        bundled_data: Optional[Dict[str, bytes]] = None,
        extra_labware: Optional[Dict[str, LabwareDefinition]] = None,
        hardware_simulator: Optional[ThreadManagedHardware] = None,
        *,
        robot_type: Optional[str] = "Flex",  # Default to Flex
        use_virtual_hardware: bool = True,
    ) -> ProtocolContext:
        """
        A patched version of `get_protocol_api` that allows dynamic robot type selection.
        """
        print(f"[INFO] Using FlexibleSimulate `get_protocol_api` with robot type: {robot_type}")
        protocol_context = original_get_protocol_api(
            version,
            bundled_labware=bundled_labware,
            bundled_data=bundled_data,
            extra_labware=extra_labware,
            hardware_simulator=hardware_simulator,
            robot_type=robot_type,
            use_virtual_hardware=use_virtual_hardware,
        )
        protocol_context.robot_type = robot_type  # Set the selected robot type
        return protocol_context

    @staticmethod
    def simulate(
        protocol_file: Optional[Union[str, "TextIO"]],
        robot_type: str = "Flex",  # Default to Flex
        *args,
        **kwargs,
    ):
        """
        Wrapper for the `simulate` function to allow dynamic robot type selection.
        """
        print(f"[INFO] Simulating protocol with robot type: {robot_type}")
        # Open the protocol file if it's a file path string
        if isinstance(protocol_file, str):
            with open(protocol_file, 'r') as protocol_file_obj:
                return original_simulate(protocol_file_obj, *args, **kwargs)
        # Use the provided file-like object if already opened
        return original_simulate(protocol_file, *args, **kwargs)
