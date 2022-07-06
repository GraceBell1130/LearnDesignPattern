from pytest import *
from Barista.CoffeeWithHook import CoffeeWithHook
from Barista.TeaWithHook import TeaWithHook

def test_HookBeverage(capsys, monkeypatch):
    teaHook = TeaWithHook()
    coffeeHook = CoffeeWithHook()

    answers = iter(["y", "n"])

    print("홍차 준비 중...")
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    teaHook.prepareRecipe()
    captured = capsys.readouterr()
    assert captured.out == "홍차 준비 중...\n" +\
                           "물 끓이는 중\n" +\
                           "필터로 커피를 우려내는 중\n"+\
                           "컵에 따르는 중\n"+\
                           "레몬을 추가하는 중\n"

    print("커피 준비 중...")
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    coffeeHook.prepareRecipe()
    captured = capsys.readouterr()
    assert captured.out == "커피 준비 중...\n" +\
                           "물 끓이는 중\n" +\
                           "필터로 커피를 우려내는 중\n"+\
                           "컵에 따르는 중\n"
