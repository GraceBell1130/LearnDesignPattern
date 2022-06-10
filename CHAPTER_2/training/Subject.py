from abc import *
from Observer import *

class ISubject(ABC):
    @abstractmethod
    def registerObserver(self, o :IObserver):
        pass
        
    @abstractmethod
    def removeObserver(self, o :IObserver):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass
