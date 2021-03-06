__author__ = "nikolojedison & auxchar"
#Code copied from 2015_Lopez_Jr. Some changes to fit with 2016 setup.

import wpilib

from utilities.settings import Settings

def precision_mode(controller_input, trigger):
    """copied from CubertPy and tweaked for 2016 use."""

    if trigger == True:
        #if the trigger is pulled, start precision mode (with a slight holdover from dual-precision days):
        return controller_input * Settings.num_precision_one
    else:
        #if none are held, just return straight controller_input:
        return controller_input

def exponential_scaling(base, exponent):
    """Behold, exponents that don't die with negative values."""

    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def dead_zone(controller_input, dead_zone):
    """Old-style dead zone scaling, used on the tilt."""

    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, trigger):
    """Final y-axis thing that's used by the drivetrain class."""

    return precision_mode(exponential_scaling(exponential_scaling(controller_input, 0.5)*0.5, 1.1), trigger)

def twist_control(controller_input, trigger):
    """Final spin thing that's used by the drivetrain class."""

    return precision_mode(exponential_scaling(exponential_scaling(controller_input, 0.5)*0.5, 2.3), trigger)

def tilt_control(controller_input, trigger):
    """Final tilt thing that's used by manualTilt. Probably could be cleaned up, but oh well."""

    return precision_mode(controller_input, trigger)
