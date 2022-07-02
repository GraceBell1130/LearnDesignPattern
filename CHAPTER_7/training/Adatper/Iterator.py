from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def hasNext():
        pass
    
    @abstractmethod
    def next():
        pass

    @abstractmethod
    def remove():
        pass