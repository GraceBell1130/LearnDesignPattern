from pytest import *
from Beverage import *
from Condiment import *

def test_Espreesso():
    beverage:Beverage = Espreesso()
    assert f"{beverage.description} ${beverage.cost():0.2f}" == "에스프레소 $1.99"

def test_DarkRoast():
    beverage2:Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    assert f"{beverage2.description} ${beverage2.cost():0.2f}" == "다크 로스트 커피, 모카, 모카, 휘핑크림 $1.49"

def test_HouseBlend():
    beverage3:Beverage = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    assert f"{beverage3.description} ${beverage3.cost():0.2f}" == "하우스 블랜드 커피, 두유, 모카, 휘핑크림 $1.34"

def test_HouseBlendWithSize():
    beverage3:Beverage = HouseBlend()
    beverage3.size = Size.VENTI
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    assert f"{beverage3.description} ${beverage3.cost():0.2f}" == "하우스 블랜드 커피, 두유, 모카, 휘핑크림 $1.44"