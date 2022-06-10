from abc import *
from enum import Enum

class Size(Enum):
    TALL = 0,
    GRANDE = 1,
    VENTI = 2

class Beverage(ABC):
    def __init__(self) -> None:
        self._description :str = "제목 없음"
        self._size :Size = Size.TALL
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description :str):
        self._description = description

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: Size):
        self._size = size

    @abstractmethod
    def cost(self):
        pass

class Espreesso(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "에스프레소"
    
    def cost(self) -> float:
        return 1.99 

class HouseBlend(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "하우스 블랜드 커피"
    
    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.description = "다크 로스트 커피"
    
    def cost(self) -> float:
        return 0.99

