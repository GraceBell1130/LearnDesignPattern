from abc import ABC, abstractmethod
from typing import final

class CaffeineBeverageWithHook(ABC): 
    @final
    def prepareRecipe(self) -> None:
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def addCondiments(self) -> None:
        pass

    def boilWater(self) -> None:
        print("물 끓이는 중")
    
    def pourInCup(self) -> None:
        print("컵에 따르는 중")
    
    def customerWantsCondiments(self) -> bool:
        return True
    
