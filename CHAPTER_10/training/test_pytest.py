from __future__ import annotations
from random import seed
from pytest import *
from GumballMachine import GumballMachine
from State.StateGumballMachine import StateGumballMachine

def test_GumballMachine(capsys):
    gumballMachine :GumballMachine = GumballMachine(5)

    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 5개\n" +\
                           "동전 투입 대기중\n\n" 

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 4개\n" +\
                           "동전 투입 대기중\n\n"

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "동전이 반환됩니다.\n" +\
                           "동전을 넣어 주세요.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 4개\n" +\
                           "동전 투입 대기중\n\n"

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "동전을 넣어 주세요.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 2개\n" +\
                           "동전 투입 대기중\n\n"

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "동전은 한 개만 넣어 주세요.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "더 이상 알맹이가 없습니다.\n" +\
                           "매진되었습니다. 다음 기회에 이용해 주세요.\n" +\
                           "매진되었습니다.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 0개\n" +\
                           "매진\n\n"

def test_StateGumballMachine(capsys):
    seed(1)
    gumballMachine :StateGumballMachine = StateGumballMachine(5)
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 5개\n" +\
                           "동전 투입 대기중\n\n" 

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 4개\n" +\
                           "동전 투입 대기중\n\n"

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "동전이 반환됩니다.\n" +\
                           "동전을 넣어 주세요.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 4개\n" +\
                           "동전 투입 대기중\n\n"

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "동전을 넣으셨습니다.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "동전을 넣어 주세요.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 2개\n" +\
                           "동전 투입 대기중\n\n"
    seed(2)
    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    captured = capsys.readouterr()
    assert captured.out == "동전을 넣으셨습니다.\n" +\
                           "동전은 한 개만 넣어 주세요.\n" +\
                           "손잡이를 돌리셨습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "축하드립니다! 알맹이를 하나 더 받으실 수 있습니다.\n" +\
                           "알맹이를 내보내고 있습니다.\n" +\
                           "더 이상 알맹이가 없습니다.\n" +\
                           "매진되었습니다. 다음 기회에 이용해 주세요.\n" +\
                           "매진되었습니다.\n" +\
                           "매진되었습니다. 다음 기회에 이용해 주세요.\n" +\
                           "매진되었습니다.\n" +\
                           "\n주식회사 왕뽑기\n" +\
                           "파이썬으로 돌아가는 최신형 뽑기 기계\n" +\
                           "남은 개수: 0개\n" +\
                           "매진\n\n"