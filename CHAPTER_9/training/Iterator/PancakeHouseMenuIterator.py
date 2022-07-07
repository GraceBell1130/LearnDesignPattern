from typing import List
from Iterator.MenuItem import MenuItem
from Iterator.Iterator import Iterator

class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items :List[MenuItem]) -> None:
        super().__init__()
        self.items = items
        self.position = 0

    def next(self) -> object:
        menuItem :MenuItem = self.items[self.position]
        self.position += 1
        return menuItem
  
    def hasNext(self) -> bool:
        if self.position >= len(self.items):
            return False
        else:
            return True
            
    def remove(self) -> None:
        return super().remove()