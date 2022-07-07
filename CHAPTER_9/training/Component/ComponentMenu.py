from typing import List
from Component.MenuComponent import MenuComponent

class ComponentMenu(MenuComponent):
    def __init__(self, name :str, description :str) -> None:
        super().__init__()
        self.name :str = name
        self.description :str = description
        self.menuComponents :List[MenuComponent] = list()

    def add(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.remove(menuComponent)

    def getChild(self, i: int) -> MenuComponent:
        return self.menuComponents[i]

    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def getPrice(self) -> float:
        return super().getPrice()
    
    def isVegetarian(self) -> bool:
        return super().isVegetarian()

    def print(self) -> None:
        print(f"\n{self.getName()}",end="")
        print(f", {self.getDescription()}")
        print(f"--------------------")

        for menuComponent in self.menuComponents:
            menuComponent.print()