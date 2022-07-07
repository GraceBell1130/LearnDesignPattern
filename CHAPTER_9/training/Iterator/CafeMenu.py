from Iterator.Menu import Menu
from Iterator.MenuItem import MenuItem
from Iterator.Iterator import Iterator
from Iterator.CafeMenuIterator import CafeMenuIterator
from typing import Dict
class CafeMenu(Menu):
    def __init__(self) -> None:
        self.menuItems :Dict[str, MenuItem] = dict()
        self.addItem("베지 버거와 에어 프라이", "통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거", True, 3.99)
        self.addItem("오늘의 스프", "샐러드가 곁들여진 오늘의 스프", False, 3.69)
        self.addItem("부리토", "통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토", True, 4.29)

    def addItem(self, name :str, description: str, vegetarian: bool, price :float) -> None:
        menuItem :MenuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems[name] = menuItem
        
    def createIterator(self) -> Iterator:
        return CafeMenuIterator(self.menuItems)