from Commander.Command import Command
from Receiver.TV import TV

class TvOnCommand(Command):
    def __init__(self, tv :TV) -> None:
        self.tv :TV= tv

    def execute(self):
        self.tv.on()
        self.tv.setDVD()

    def undo(self):
        return super().undo()

class TvOffCommand(Command):
    def __init__(self, tv :TV) -> None:
        self.tv :TV= tv

    def execute(self):
        self.tv.off()
     
    def undo(self):
        return super().undo()