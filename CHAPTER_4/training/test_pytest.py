from pytest import *
from PizzaStore import *

def test_OrderFromEdan(capsys):
    nyStore : PizzaStore = NYStylePizzaStore()
    pizza :Pizza = nyStore.orderPizza("cheese")
    captured = capsys.readouterr()
    assert captured.out == \
        "준비 중: 뉴욕 스타일 소스와 치즈 피자\n" \
        + "도우를 돌리는 중...\n"\
        + "소스를 뿌리는 중...\n"\
        + "토핑을 올리는 중...\n"\
        + "\t잘게 썬 레지아노 치즈\n"\
        + "175도에서 25분 간 굽기\n"\
        + "피자를 사선으로 자르기\n"\
        + "상자에 피자 담기\n"

    check_order = f"에단이 주문한 {pizza.getName()}"
    assert "에단이 주문한 뉴욕 스타일 소스와 치즈 피자" == check_order

def test_OrderFromJoel(capsys):
    chicagoStore : PizzaStore = ChicagoStylePizzaStore()
    pizza :Pizza = chicagoStore.orderPizza("cheese")
    captured = capsys.readouterr()
    assert captured.out == \
        "준비 중: 시카고 스타일 딥 디쉬 치즈 피자\n" \
        + "도우를 돌리는 중...\n"\
        + "소스를 뿌리는 중...\n"\
        + "토핑을 올리는 중...\n"\
        + "\t잘게 조각낸 모짜렐라 치즈\n"\
        + "175도에서 25분 간 굽기\n"\
        + "네모난 모양으로 피자 자르기\n"\
        + "상자에 피자 담기\n"
    check_order = f"조엘이 주문한 {pizza.getName()}"
    assert "조엘이 주문한 시카고 스타일 딥 디쉬 치즈 피자" == check_order
