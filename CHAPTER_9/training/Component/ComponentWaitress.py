from Component.MenuComponent import MenuComponent

class ComponentWaitress():
    def __init__(self, allMenu :MenuComponent) -> None:
        self.allMenus :MenuComponent = allMenu

    def printMenu(self) -> None:
        self.allMenus.print()