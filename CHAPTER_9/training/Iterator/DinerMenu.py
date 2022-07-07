from typing import List
from Iterator.Menu import Menu
from Iterator.MenuItem import MenuItem
from Iterator.Iterator import Iterator
from Iterator.DinerMenuIterator import DinerMenuIterator

MAX_ITEMS :int = 6

class DinerMenu(Menu):
    def __init__(self) -> None:
        self.numberOfItems = 0
        self.menuItems :List[MenuItem] = [None] * MAX_ITEMS


        self.addItem("채식주의자용 BLT", "통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴", True, 2.99)
        self.addItem("BLT", "통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴", False, 2.99)
        self.addItem("오늘의 스프", "감자 샐러드를 곁들인 오늘의 스프", False, 3.29)
        self.addItem("핫도그", "사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그", False, 3.05)

    def addItem(self, name :str, description: str, vegetarian: bool, price :float) -> None:
        menuItem :MenuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems >= MAX_ITEMS:
            print("죄송합니다, 메뉴가 꽉 찼습니다. 더 이상 추가할 수 없습니다.")
        else:
            self.menuItems[self.numberOfItems] = menuItem
            self.numberOfItems += 1
    
    def createIterator(self) -> Iterator:
        return DinerMenuIterator(self.menuItems)

    def getMenuItems(self) -> List[MenuItem]:
        return self.menuItems

    def __str__(self) -> str:
        return "Diner Menu"
