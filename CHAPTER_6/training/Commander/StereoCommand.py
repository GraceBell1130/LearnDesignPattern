from Commander.Command import Command
from Receiver.Stereo import Stereo

class StereoOnCommand(Command):
    def __init__(self, stereo :Stereo) -> None:
        self.stereo :Stereo= stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

    def undo(self):
        return super().undo()

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo :Stereo) -> None:
        self.stereo :Stereo= stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

    def undo(self):
        return super().undo()

class StereoOffCommand(Command):
    def __init__(self, stereo :Stereo) -> None:
        self.stereo :Stereo= stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        return super().undo()