from abc import ABC, abstractmethod

class GumballMachineRemote(ABC):
    @abstractmethod
    def getCount() -> int:
        pass

    @abstractmethod
    def getLocation() -> str:
        pass

    @abstractmethod
    def getState() -> object:
        pass

