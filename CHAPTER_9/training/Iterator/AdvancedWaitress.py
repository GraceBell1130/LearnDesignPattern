from typing import List
from Iterator.Iterator import Iterator
from Iterator.Menu import Menu
from Iterator.MenuItem import MenuItem

class AdvancedWaitress():
    def __init__(self, menus :List[Menu]) -> None:
        self.menus :List[Menu] = menus

    def printMenu(self) -> None:
        menuIterator :Iterator = iter(self.menus)
        while menuIterator.hasNext():
            menu :Menu = menuIterator.next()
            self.printMenuIterator(menu)

    def printMenuIterator(self, iterator: Iterator) -> None:
        while iterator.hasNext():
            menuItem :MenuItem = iterator.next()
            print(f"{menuItem.getName()}, ", end="")
            print(f"{menuItem.getPrice()} -- ", end="")
            print(f"{menuItem.getDescription()}")
