from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass

class MacroCommand(Command):
    def __init__(self, commands :List[Command]) -> None:
        self.commands :List[Command] = commands

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()

    def undo(self):
        for i in range(len(self.commands) - 1, 0, -1):
            self.commands[i].undo()