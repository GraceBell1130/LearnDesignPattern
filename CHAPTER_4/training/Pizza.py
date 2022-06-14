from abc import ABC
from typing import List

class Pizza(ABC):
    def __init__(self) -> None:
        self.name :str = None
        self.dough :str = None
        self.sauce :str = None
        self.toppings :List[str] = list()

    def prepare(self) -> None:
        print(f"준비 중: {self.name}")
        print("도우를 돌리는 중...")
        print("소스를 뿌리는 중...")
        print("토핑을 올리는 중...")
        for topping in self.toppings:
            print(f"\t{topping}")

    def bake(self) -> None:
        print("175도에서 25분 간 굽기")

    def cut(self) -> None:
        print("피자를 사선으로 자르기")

    def box(self) -> None:
        print("상자에 피자 담기")

    def getName(self) -> str:
        return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "뉴욕 스타일 소스와 치즈 피자"
        self.dough = "씬 크러스트 도우"
        self.sauce = "마리나라 소스"

        self.toppings.append("잘게 썬 레지아노 치즈")

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "시카고 스타일 딥 디쉬 치즈 피자"
        self.dough = "아주 두꺼운 크러스트 도우"
        self.sauce = "플럼토마토 소스"
        
        self.toppings.append("잘게 조각낸 모짜렐라 치즈")

    def cut(self):
        print("네모난 모양으로 피자 자르기")


class SimplePizzaFactory():
    def createPizza(pizza_type :str) -> Pizza:
        pizza :Pizza = None

        if pizza_type == "cheese":
            pass
        elif pizza_type == "pepperoni":
            pass
        elif pizza_type == "clam":
            pass
        elif pizza_type == "veggie":
            pass

        return pizza