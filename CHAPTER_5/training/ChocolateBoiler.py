from multiprocessing import Lock


class ChocolateBoiler(object):
    empty :bool = True
    boiled :bool = True
    lock = Lock()
    __instance = None

    def __new__(cls):
        cls.lock.acquire()
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        cls.lock.release()
        return cls.__instance

    def fill(self) -> None:
        if self.isEmpty():
            ChocolateBoiler.empty = False
            ChocolateBoiler.boiled = False

    def drain(self) -> None:
        if not self.isEmpty() and self.isBoiled():
            ChocolateBoiler.empty = True
        
    def boil(self) -> None:
        if not self.isEmpty() and not self.isBoiled():
            ChocolateBoiler.boiled = True
        
    def isEmpty(self) -> bool:
        return ChocolateBoiler.empty

    def isBoiled(self) -> bool:
        return ChocolateBoiler.boiled

    