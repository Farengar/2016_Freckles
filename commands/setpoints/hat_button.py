__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.hat import Hat

class HatButton(Command):
    def __init__(self, robot, output):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.hat)
        self.output = output

    def execute(self):
        self.robot.hat.manualSet(self.output)

    def isFinished(self):
        return False

    def end(self):
        self.robot.hat.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
