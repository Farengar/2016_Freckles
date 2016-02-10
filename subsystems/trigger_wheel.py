__author__ = "nikolojedison"

import wpilib
from wpilib.command import Subsystem
from utilities.settings import Settings
from commands.manual.manual_trigger import ManualTrigger

class TriggerWheel(Subsystem):
    """Run the trigger wheel."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.motor = wpilib.CANTalon(1)

    def initDefaultCommand(self):
        pass

    def manualSet(self, output):
        self.motor.set(output)

    def log(self):
        pass
