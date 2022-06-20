from Commander.Command import Command
from Receiver.Light import Light

class LightOnCommand(Command):
    def __init__(self, light :Light):
        self.light:Light = light

    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light :Light) -> None:
        self.light:Light = light

    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()