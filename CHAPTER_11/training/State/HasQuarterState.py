from random import randint
from State.State import State
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from State.StateGumballMachine import StateGumballMachine
    
class HasQuarterState(State):
    def __init__(self, gumballMachine :'StateGumballMachine') -> None:
        self.gumballMachine :StateGumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("동전은 한 개만 넣어 주세요.")
    
    def ejectQuarter(self) -> None:
        print("동전이 반환됩니다.")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    
    def turnCrank(self) -> None:
        print("손잡이를 돌리셨습니다.")
        if self.gumballMachine.getCount() > 1 and randint(0, 9) is 0:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else: 
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self) -> None:
        print("알맹이를 내보낼 수 없습니다.")

    def __str__(self) -> str:
        return "손잡이 돌리기를 대기중"