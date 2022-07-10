from State.State import State
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from State.StateGumballMachine import StateGumballMachine

class WinnerState(State):
    def __init__(self, gumballMachine :'StateGumballMachine') -> None:
        self.gumballMachine :StateGumballMachine = gumballMachine

    def insertQuarter(self) -> None:
        print("알맹이를 내보내고 있습니다.")
    
    def ejectQuarter(self) -> None:
        print("이미 알맹이를 뽑으셨습니다.")

    def turnCrank(self) -> None:
        print("손잡이는 한 번만 돌려 주세요.")

    def dispense(self) -> None:
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() is 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())
        else:
            print("축하드립니다! 알맹이를 하나 더 받으실 수 있습니다.")
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("더 이상 알맹이가 없습니다.")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def refill(self) -> None:
        pass
    
    def __str__(self) -> str:
        return "알맹이 전달중"