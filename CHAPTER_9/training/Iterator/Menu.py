from abc import ABC, abstractmethod
from Iterator.Iterator import Iterator

class Menu(ABC):
    @abstractmethod
    def createIterator(self) -> Iterator:
        pass