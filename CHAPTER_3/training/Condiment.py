from abc import *
from Beverage import *

class CondimentDecorator(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.beverage :Beverage = None

    def getSize(self):
        return self.beverage.size

    @Beverage.description.getter
    @abstractstaticmethod
    def description(self):
        pass

class Mocha(CondimentDecorator):
    def __init__(self, beverage :Beverage) -> None:
        super().__init__()
        self.beverage = beverage
    
    @CondimentDecorator.description.getter
    def description(self):
        return self.beverage.description + ", 모카"

    def cost(self):
        return self.beverage.cost() + 0.20

class Soy(CondimentDecorator):
    def __init__(self, beverage :Beverage) -> None:
        super().__init__()
        self.beverage = beverage
    
    @CondimentDecorator.description.getter
    def description(self):
        return self.beverage.description + ", 두유"

    def cost(self):
        if self.getSize() == Size.TALL:
            return self.beverage.cost() + 0.15
        elif self.getSize() == Size.GRANDE:
            return self.beverage.cost() + 0.20
        else:
            return self.beverage.cost() + 0.25

class Whip(CondimentDecorator):
    def __init__(self, beverage :Beverage) -> None:
        super().__init__()
        self.beverage = beverage
    
    @CondimentDecorator.description.getter
    def description(self):
        return self.beverage.description + ", 휘핑크림"

    def cost(self):
        return self.beverage.cost() + 0.10
