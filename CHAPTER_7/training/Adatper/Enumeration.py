from abc import ABC, abstractmethod

class Enumeration(ABC):
    @abstractmethod
    def hasMoreElements():
        pass

    @abstractmethod
    def nextElement():
        pass