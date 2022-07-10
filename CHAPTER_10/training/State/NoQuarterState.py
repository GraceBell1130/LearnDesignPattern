from State.State import State
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from State.StateGumballMachine import StateGumballMachine
    
class NoQuarterState(State):
    def __init__(self, gumballMachine :'StateGumballMachine') -> None:
        self.gumballMachine :StateGumballMachine = gumballMachine

    def insertQuarter(self) -> None:
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
        print("동전을 넣으셨습니다.")
    
    def ejectQuarter(self) -> None:
        print("동전을 넣어 주세요.")

    def turnCrank(self) -> None:
        print("동전을 넣어 주세요.")

    def dispense(self) -> None:
        pass

    def __str__(self) -> str:
        return "동전 투입 대기중"