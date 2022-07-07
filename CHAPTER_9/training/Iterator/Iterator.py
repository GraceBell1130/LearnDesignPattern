


from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def hasNext(self)-> bool:
        pass
    
    @abstractmethod
    def next(self) -> object:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass