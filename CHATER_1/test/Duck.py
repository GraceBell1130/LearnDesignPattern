from abc import *
from Quack import *
from Fly import *

class Duck(ABC):
    def __init__(self) -> None:
        self.__quackBehavior: QuackBehavior
        self.__flyBehavior: FlyBehavior
    
    @abstractmethod
    def display(self):
        pass

    @property
    def flyBehavior(self):
        return self.__flyBehavior

    @flyBehavior.setter
    def flyBehavior(self, fb :FlyBehavior):
        self.__flyBehavior = fb

    @property
    def quackBehavior(self):
        return self.__quackBehavior
        
    @quackBehavior.setter
    def quackBehavior(self, qb :QuackBehavior):
        self.__quackBehavior = qb

    def performFly(self):
        self.__flyBehavior.fly()

    def performQuack(self):
        self.__quackBehavior.quack()
    
    def setFlyBehavior(self, fb :FlyBehavior):
        self.__flyBehavior = fb

    def setquackBehavior(self, qb :QuackBehavior):
        self.__quackBehavior = qb

    def swim(self):
        print("모든 오리는 물에 뜹니다. 가짜 오리도 뜨죠")

class MallardDuck(Duck):
    def __init__(self) -> None:
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("저는 물오리입니다.")

class ModelDuck(Duck):
    def __init__(self) -> None:
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()
    
    def display(self):
        print("저는 모형 오리입니다.")