from typing import List
from Iterator.Menu import Menu
from Iterator.MenuItem import MenuItem
from Iterator.Iterator import Iterator
from Iterator.PancakeHouseMenuIterator import PancakeHouseMenuIterator

class PancakeHouseMenu(Menu):
    def __init__(self) -> None:
        self.menuItems :List[MenuItem] = list()
        self.addItem("K&B 팬케이크 세트", "스크램블 에그와 토스트가 곁들여진 팬케이크", True, 2.99)
        self.addItem("레귤러 팬케이크 세트", "달걀 프라이와 소시지가 곁들여진 팬케이크", False, 2.99)
        self.addItem("블루베리 팬케이크", "신선한 블루베리와 블루베리 시럽으로 만든 팬케이크", True, 3.49)
        self.addItem("와플", "취향에 따라 블루베리나 딸기를 얹을 수 있는 와플", True, 3.59)

    def addItem(self, name :str, description: str, vegetarian: bool, price :float) -> None:
        menuItem :MenuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)

    def getMenuItems(self) -> List[MenuItem]:
        return self.menuItems
    
    def createIterator(self) -> Iterator:
        return PancakeHouseMenuIterator(self.menuItems)

    def __str__(self) -> str:
        return "Pancake House Menu"
