from pytest import *
from State.GumballMonitor import GumballMonitor
from State.StateGumballMachine import StateGumballMachine

def test_GumballMachineMonitor(capsys):  
   gumballMachine :StateGumballMachine = StateGumballMachine("Austin", 112)
   monitor :GumballMonitor = GumballMonitor(gumballMachine)

   monitor.report()
   captured = capsys.readouterr()
   assert captured.out == "뽑기 기계 위치: Austin\n" +\
                        "현재 재고: 112 개\n" +\
                        "현재 상태: 동전 투입 대기중\n"
                        