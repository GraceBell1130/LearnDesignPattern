from typing import Dict, List
from Iterator.Iterator import Iterator
from Iterator.MenuItem import MenuItem

class CafeMenuIterator(Iterator):
    def __init__(self, items: Dict[str, MenuItem]) -> None:
        super().__init__()
        self.items :List[MenuItem] = list(items.values())
        self.position :int = 0

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