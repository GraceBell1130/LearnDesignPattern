from State.State import State
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from State.StateGumballMachine import StateGumballMachine
    
class SoldOutState(State):
    def __init__(self, gumballMachine :'StateGumballMachine') -> None:
        self.gumballMachine :StateGumballMachine = gumballMachine

    def insertQuarter(self) -> None:
        print("매진되었습니다. 다음 기회에 이용해 주세요.")
    
    def ejectQuarter(self) -> None:
        print("동전을 넣지 않으셨습니다. 동전이 반환되지 않습니다.")

    def turnCrank(self) -> None:
        print("매진되었습니다.")

    def dispense(self) -> None:
        pass

    def refill(self) -> None:
        pass
    
    def __str__(self) -> str:
        return "매진"