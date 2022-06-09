from abc import *

class IDisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

