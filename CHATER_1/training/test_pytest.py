from Duck import *
from pytest import *


def test_mallardDuck(capsys):
    mallard = MallardDuck()
    mallard.performQuack()
    captured = capsys.readouterr()
    assert captured.out == "꽥\n"
    mallard.performFly()
    captured = capsys.readouterr()
    assert captured.out == "날고 있어요!!\n"

def test_modelDuck(capsys):
    model = ModelDuck()
    model.performFly()
    captured = capsys.readouterr()
    assert captured.out == "저는 못 날아요\n"
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()
    captured = capsys.readouterr()
    assert captured.out == "로켓 추진으로 날아갑니다.\n"
