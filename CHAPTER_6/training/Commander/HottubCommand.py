from Commander.Command import Command
from Receiver.Hottub import Hottub

class HottubOnCommand(Command):
    def __init__(self, hottub :Hottub) -> None:
        self.hottub :Hottub = hottub

    def execute(self):
        self.hottub.on()
        self.hottub.setTemperature(40)
        self.hottub.getTemperature()

    def undo(self):
        return super().undo()

class HottubOffCommand(Command):
    def __init__(self, hottub :Hottub) -> None:
        self.hottub :Hottub = hottub

    def execute(self):
        self.hottub.setTemperature(36)

    def undo(self):
        return super().undo()