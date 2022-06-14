from typing import final
from Pizza import *
from abc import ABC, abstractmethod

class PizzaStore(ABC):
    @final
    def orderPizza(self, pizza_type :str) -> Pizza:
        pizza :Pizza

        pizza = self.createPizza(pizza_type)

        pizza.prepare()        
        pizza.bake()        
        pizza.cut()        
        pizza.box()

        return pizza        

    @abstractmethod
    def createPizza(self, pizza_type:str) -> Pizza:
        pass


class NYStylePizzaStore(PizzaStore):
    def createPizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        
        return None

class ChicagoStylePizzaStore(PizzaStore):
    def createPizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
            
        return None