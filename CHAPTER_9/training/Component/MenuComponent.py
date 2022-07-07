from __future__ import annotations
from abc import ABC, abstractmethod
from io import UnsupportedOperation

class MenuComponent(ABC):
    @abstractmethod
    def add(self, menuComponent: MenuComponent) -> None:
        raise UnsupportedOperation()

    @abstractmethod
    def remove(self, menuComponent: MenuComponent) -> None:
        raise UnsupportedOperation()

    @abstractmethod
    def getChild(self, i :int) -> MenuComponent:
        raise UnsupportedOperation()

    @abstractmethod
    def getName(self) -> str:
        raise UnsupportedOperation()

    @abstractmethod
    def getDescription(self) -> str:
        raise UnsupportedOperation()

    @abstractmethod
    def getPrice(self) -> float:
        raise UnsupportedOperation()

    @abstractmethod
    def isVegetarian(self) -> bool:
        raise UnsupportedOperation()

    @abstractmethod
    def print(self) -> None:
        raise UnsupportedOperation()
