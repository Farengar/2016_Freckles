__author__ = "nikolojedison"

import wpilib
from wpilib.buttons import JoystickButton, InternalButton
from networktables import NetworkTable

from utilities.pov_button import POVButton
from utilities.drive_control import *
from utilities.settings import Settings

from macros.play_macro import PlayMacro
from macros.record_macro import RecordMacro

from commands.setpoints.hat_button import HatButton
from commands.setpoints.ears_button import EarsButton
from commands.setpoints.tilt_bottom import TiltBottom
from commands.setpoints.tilt_ramp import TiltRamp
from commands.setpoints.tilt_shoot import TiltShoot
from commands.setpoints.tilt_top import TiltTop

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        """Double joysticks WOOT"""

        #initialise the stick and the smart dashboard (in case we need stuff for auton):
        self.stick = wpilib.Joystick(0)
        self.setpointStick = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Main stick buttons.
        #-----------------------------------------------------------------------
        good_trigger = JoystickButton(self.stick, 1)
        thumb_stripe = JoystickButton(self.stick, 2)
        trigger_bumper = JoystickButton(self.stick, 3)
        thumb_normal = JoystickButton(self.stick, 4)

        #Throttle buttons.
        #-----------------------------------------------------------------------
        throttle_five = JoystickButton(self.stick, 5)
        throttle_six = JoystickButton(self.stick, 6)
        throttle_seven = JoystickButton(self.stick, 7)
        throttle_eight = JoystickButton(self.stick, 8)
        throttle_nine = JoystickButton(self.stick, 9)
        throttle_ten = JoystickButton(self.stick, 10)

        #Hat switch POV stuff.
        #-----------------------------------------------------------------------
        pov_north = POVButton(self.stick, 0)
        pov_northeast = POVButton(self.stick, 45)
        pov_east = POVButton(self.stick, 90)
        pov_southeast = POVButton(self.stick, 135)
        pov_south = POVButton(self.stick, 180)
        pov_southwest = POVButton(self.stick, 225)
        pov_west = POVButton(self.stick, 270)
        pov_northwest = POVButton(self.stick, 315)


        #Setpoint stick button mapping.
        #-----------------------------------------------------------------------
        bad_trigger = JoystickButton(self.setpointStick, 1)
        thumb = JoystickButton(self.setpointStick, 2)
        bottom_left = JoystickButton(self.setpointStick, 3)
        bottom_right = JoystickButton(self.setpointStick, 4)
        top_left = JoystickButton(self.setpointStick, 5)
        top_right = JoystickButton(self.setpointStick, 6)


        #goes from front to back. outer_base is the outer ring of buttons on
        #the base, inner_base is the inner ring of buttons on the base.
        #-----------------------------------------------------------------------
        outer_base_one = JoystickButton(self.setpointStick, 7)
        inner_base_one = JoystickButton(self.setpointStick, 8)
        outer_base_two = JoystickButton(self.setpointStick, 9)
        inner_base_two = JoystickButton(self.setpointStick, 10)
        outer_base_three = JoystickButton(self.setpointStick, 11)
        inner_base_three = JoystickButton(self.setpointStick, 12)

        #-----------------------------------------------------------------------

        #Mapping of buttons.
        #-----------------------------------------------------------------------
        thumb_stripe.whileHeld(EarsButton(robot, .5))
        good_trigger.whileHeld(HatButton(robot, .5))
        thumb_normal.whileHeld(EarsButton(robot, -.5))
        trigger_bumper.whileHeld(HatButton(robot, -.5))
        outer_base_one.whileHeld(TiltTop(robot))
        outer_base_two.whileHeld(TiltShoot(robot))
        outer_base_three.whileHeld(TiltTop(robot))
        inner_base_two.whileHeld(TiltRamp(robot))


    def getStick(self):
        """Drive joystick."""
        return self.stick

    def getSetpointStick(self):
        """Button joystick."""
        return self.setpointStick
