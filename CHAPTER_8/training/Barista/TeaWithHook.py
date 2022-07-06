from Barista.CaffeineBeverageWithHook import CaffeineBeverageWithHook


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("필터로 커피를 우려내는 중")

    def addCondiments(self) -> None:
        print("레몬을 추가하는 중")

    def customerWantsCondiments(self) -> bool:
        answer :str = self.__getUserInput()
        
        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def __getUserInput(self) -> str:
        answer = input("차에 레몬을 넣을까요? (y/n)? ")
        return answer
