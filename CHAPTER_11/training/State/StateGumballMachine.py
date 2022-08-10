from __future__ import annotations
from State.State import State
from State.HasQuarterState import HasQuarterState
from State.SoldState import SoldState
from State.NoQuarterState import NoQuarterState
from State.SoldOutState import SoldOutState
from State.WinnerState import WinnerState
class StateGumballMachine():
    def __init__(self, location :str, count :int) -> None:
        self.soldState :State = SoldState(self)
        self.hasQuarterState :State = HasQuarterState(self)
        self.noQuarterState :State = NoQuarterState(self)
        self.soldOutState :State = SoldOutState(self)
        self.winnerState :State = WinnerState(self)

        self.state :State = None
        self.count :int = count
        self.location :str = location
        if self.count > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState

    def insertQuarter(self) -> None:
        self.state.insertQuarter()

    def ejectQuarter(self) -> None:
        self.state.ejectQuarter()

    def turnCrank(self) -> None:
        self.state.turnCrank()
        self.state.dispense()
        
    def refill(self, numGumBalls :int) -> None:
        self.count = numGumBalls
        self.state = self.NO_QUARTER

    def releaseBall(self) -> None:
        print("알맹이를 내보내고 있습니다.")
        if self.count > 0:
            self.count -= 1

    def setState(self, state: State) -> None:
        self.state = state

    def getCount(self) -> int:
        return self.count

    def getLocation(self) -> str:
        return self.location

    def getState(self) -> State:
        return self.state

    def getHasQuarterState(self) -> HasQuarterState:
        return self.hasQuarterState

    def getSoldState(self) -> SoldState:
        return self.soldState

    def getNoQuarterState(self) -> NoQuarterState:
        return self.noQuarterState

    def getSoldOutState(self) -> SoldOutState:
        return self.soldOutState

    def getWinnerState(self) -> WinnerState:
        return self.winnerState

    def __str__(self) -> str:
        result :str = ""
        result += "\n주식회사 왕뽑기"
        result += "\n파이썬으로 돌아가는 최신형 뽑기 기계\n"
        result += f"남은 개수: {self.count}개\n"
        result += f"{self.state}\n"
 
        return result