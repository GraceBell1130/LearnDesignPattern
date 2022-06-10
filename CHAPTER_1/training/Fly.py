from abc import *

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("날고 있어요!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("저는 못 날아요")
    
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("로켓 추진으로 날아갑니다.")