__author__ = "auxiliary-character"

import csv

import wpilib
from wpilib.command import Command
from wpilib.timer import Timer

from utilities.settings import Settings

class RecordMacro(Command):
    """This records robot movements and writes them to a .csv file."""
    def __init__(self, robot, name):

        super().__init__()
        self.robot = robot

        #length of time to record the macro.
        self.setTimeout(Settings.num_macro_timeout)
        self.name = name

    def initialize(self):
        """Set up the macro file and prepare for recording."""
        print("Initializing macro " + self.name + "...")

        self.initTime = wpilib.Timer.getFPGATimestamp() #get the current time
        self.f = open("/home/lvuser/py/macros/"+self.name, "w")
        fields = ["Drive_Y",
                  "Drive_Twist",
                  "Ears",
                  "Hat",
                  "Tilt",
                  "Time"]
        self.writer = csv.DictWriter(self.f, fieldnames=fields)
        self.writer.writeheader()

    def execute(self):
        """Record the macro."""

        #do the actual writing bit:
        self.writer.writerow({
            #Add subsystems in the following manner:
            #"Row_Name": self.robot.subsystem.getValue
            "Drive_Y": self.robot.drivetrain.y,
            "Drive_Twist": self.robot.drivetrain.twist,
            "Ears": self.robot.ears.right.get(),
            "Hat": self.robot.hat.motor.get(),
            "Tilt": self.robot.tilt.tilt_motor.get(),

            "Time": wpilib.Timer.getFPGATimestamp() - self.initTime}) #get the time as the row is written

    def isFinished(self):
        """Returns .isTimedOut() when called."""
        return self.isTimedOut()

    def end(self):
        """Close out & save the macro when called."""
        self.f.close()
        print("Macro recorded, filename " + self.name)

    def interrupted(self):
        """Run when macro recording is interrupted."""
        print("Macro interrupted!")

    def cancel(self):
        """Run when macro recording is canceled."""

        self.end()
        super().cancel()
