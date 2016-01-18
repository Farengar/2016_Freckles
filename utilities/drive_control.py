__author__ = "nikolojedison & auxchar"
#Code copied from 2015_Lopez_Jr.
import wpilib
from utilities.settings import Settings

def precision_mode(controller_input, button_state):
    """copied from CubertPy, b/c it worked"""

    if button_state:
        return controller_input * Settings.num_precision
    else:
        return controller_input

def exponential_scaling(base, exponent):

    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def dead_zone(controller_input, dead_zone):
    """This is the dead zone code, essential for any 4009 'bot."""

    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, button_state):
    return precision_mode(exponential_scaling(dead_zone(controller_input, 0.1), Settings.num_scaling), button_state) #the 0.75 was initially 2.3 (in case it needs to be changed)
