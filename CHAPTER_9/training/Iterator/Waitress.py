from Iterator import Iterator
from Iterator.Menu import Menu
from Iterator.MenuItem import MenuItem

class Waitress():
    def __init__(self, pancakeHouseMenu :Menu, dinerMenu: Menu, cafeMenu :Menu) -> None:
        self.pancakeHouseMenu :Menu = pancakeHouseMenu
        self.dinerMenu :Menu = dinerMenu
        self.cafeMenu :Menu = cafeMenu

    def printMenu(self) -> None:
        pancakeIterator :Iterator = self.pancakeHouseMenu.createIterator()
        dinerIterator :Iterator = self.dinerMenu.createIterator()
        cafeIterator :Iterator = self.cafeMenu.createIterator()

        print("메뉴\n----\n아침메뉴")
        self.printMenuIterator(pancakeIterator)
        print("\n점심 메뉴")
        self.printMenuIterator(dinerIterator)
        print("\n저녁 메뉴")
        self.printMenuIterator(cafeIterator)

    def printMenuIterator(self, iterator: Iterator) -> None:
        while iterator.hasNext():
            menuItem :MenuItem = iterator.next()
            print(f"{menuItem.getName()}, ", end="")
            print(f"{menuItem.getPrice()} -- ", end="")
            print(f"{menuItem.getDescription()}")
