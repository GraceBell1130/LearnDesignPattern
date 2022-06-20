from Commander.Command import Command
from Receiver.CeilingFan import CeilingFan

class CeilingFanOnCommand(Command):
    def __init__(self, ceilingFan :CeilingFan = "") -> None:
        self.ceilingFan :CeilingFan = ceilingFan

    def execute(self):
        self.ceilingFan.high()

    def undo(self):
        return super().undo()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan :CeilingFan = "") -> None:
        self.ceilingFan :CeilingFan = ceilingFan
        self.prevSpeed :CeilingFan.POWER = CeilingFan.POWER.OFF

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()
        
    def undo(self):
        if self.prevSpeed == CeilingFan.POWER.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.POWER.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.POWER.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.POWER.OFF:
            self.ceilingFan.off()



class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan :CeilingFan = "") -> None:
        self.ceilingFan :CeilingFan = ceilingFan
        self.prevSpeed :CeilingFan.POWER = CeilingFan.POWER.OFF

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        if self.prevSpeed == CeilingFan.POWER.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.POWER.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.POWER.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.POWER.OFF:
            self.ceilingFan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan :CeilingFan = "") -> None:
        self.ceilingFan :CeilingFan = ceilingFan
        self.prevSpeed :CeilingFan.POWER = CeilingFan.POWER.OFF

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == CeilingFan.POWER.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.POWER.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.POWER.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.POWER.OFF:
            self.ceilingFan.off()


class CeilingFanLowCommand(Command):
    def __init__(self, ceilingFan :CeilingFan = "") -> None:
        self.ceilingFan :CeilingFan = ceilingFan
        self.prevSpeed :CeilingFan.POWER = CeilingFan.POWER.OFF

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.low()

    def undo(self):
        if self.prevSpeed == CeilingFan.POWER.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.POWER.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.POWER.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.POWER.OFF:
            self.ceilingFan.off()

