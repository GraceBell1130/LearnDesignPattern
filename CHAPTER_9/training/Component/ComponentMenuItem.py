from Component.MenuComponent import MenuComponent

class ComponentMenuItem(MenuComponent):
    def __init__(self, name :str, description: str, vegetarian: bool, price :float) -> None:
        self.name :str = name
        self.description :str = description
        self.vegetarian :bool = vegetarian
        self.price :float = price

    def add(self, menuComponent: MenuComponent) -> None:
        return super().add(menuComponent)

    def getChild(self, i: int) -> MenuComponent:
        return super().getChild(i)

    def remove(self, menuComponent: MenuComponent) -> None:
        return super().remove(menuComponent)

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getPrice(self) -> float:
        return self.price

    def isVegetarian(self) -> bool:
        return self.vegetarian

    def print(self) -> None:
        print(f" {self.getName()}", end="")
        if self.isVegetarian():
            print("(v)", end="")
        print(f", {self.getPrice()}")
        print(f"    -- {self.getDescription()}")