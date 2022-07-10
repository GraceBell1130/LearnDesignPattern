from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insertQuarter(self) -> None:
        pass
    
    @abstractmethod
    def ejectQuarter(self) -> None:
        pass
    
    @abstractmethod
    def turnCrank(self) -> None:
        pass
    
    @abstractmethod
    def dispense(self) -> None:
        pass