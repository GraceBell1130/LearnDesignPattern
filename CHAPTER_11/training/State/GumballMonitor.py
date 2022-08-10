from State.StateGumballMachine import StateGumballMachine

class GumballMonitor():
    def __init__(self, machine :StateGumballMachine) -> None:
        self.machine :StateGumballMachine = machine

    def report(self) -> None:
        print(f"뽑기 기계 위치: {self.machine.getLocation()}")
        print(f"현재 재고: {self.machine.getCount()} 개")
        print(f"현재 상태: {self.machine.getState()}")