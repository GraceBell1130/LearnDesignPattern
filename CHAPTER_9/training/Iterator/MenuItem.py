class MenuItem():
    def __init__(self, name :str, description: str, vegetarian: bool, price :float) -> None:
        self.name :str = name
        self.description :str = description
        self.vegetarian :bool = vegetarian
        self.price :float = price

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getPrice(self) -> float:
        return self.price

    def isVegetarian(self) -> bool:
        return self.vegetarian