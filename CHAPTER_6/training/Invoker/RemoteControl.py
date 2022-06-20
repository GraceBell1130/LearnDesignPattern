from Commander.Command import Command, NoCommand

class RemoteControl():
    def __init__(self) -> None:
        self.onCommands = [Command for _ in range(7)]
        self.offCommands = [Command for _ in range(7)]
        noCommand :NoCommand = NoCommand()
        for i in range(7):
            self.onCommands[i] = noCommand
            self.offCommands[i] = noCommand

        self.undoCommand = noCommand
    
    def setCommand(self, slot:int, onCommand: Command, offCommand: Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot:int):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot:int):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPushed(self):
        self.undoCommand.undo()
        
    def __str__(self) -> str:
        stringBuff = str()
        stringBuff += "\n----- 리모컨 -----\n"
        
        for i in range(len(self.onCommands)):
            stringBuff += f"[slot {i}] {self.onCommands[i].__class__.__name__} {self.offCommands[i].__class__.__name__}\n"
        stringBuff += f"[undo] {self.undoCommand.__class__.__name__}\n"
        return stringBuff
        
