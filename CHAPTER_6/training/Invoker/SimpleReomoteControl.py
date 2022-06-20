from Commander.Command import Command

class SimpleRemoteControl():

    def __init__(self) -> None:
        self.slot :Command = None

    def setCommand(self, command: Command) -> None:
        self.slot = command
    
    def buttonWasPressed(self) -> None:
        self.slot.execute()