from Commander.Command import Command
from Receiver.GarageDoor import GarageDoor

class GarageDoorOpenCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.up()
        
    def undo(self):
        return super().undo()

class GarageDoorUpCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.up()

    def undo(self):
        return super().undo()

class GarageDoorDownCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.down()

    def undo(self):
        return super().undo()

class GarageDoorStopCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.stop()

    def undo(self):
        return super().undo()

class GarageDoorLightOnCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.lightOn()
    
    def undo(self):
        return super().undo()
class GarageDoorLightOffCommand(Command):
    def __init__(self, door: GarageDoor) -> None:
        self.door :GarageDoor = door

    def execute(self):
        self.door.lightOff()

    def undo(self):
        return super().undo()
