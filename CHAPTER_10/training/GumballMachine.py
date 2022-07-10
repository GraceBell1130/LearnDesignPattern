
class GumballMachine():
    SOLD_OUT :int = 0
    NO_QUARTER :int = 1
    HAS_QUARTER :int = 2
    SOLD :int = 3

    def __init__(self, count :int) -> None:
        self.state :int = self.SOLD_OUT
        self.count :int = count
        if self.count > 0:
            self.state = self.NO_QUARTER

    def insertQuarter(self) -> None:
        if self.state is self.HAS_QUARTER:
            print("동전은 한 개만 넣어 주세요.")
        elif self.state is self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print("동전을 넣으셨습니다.")
        elif self.state is self.SOLD_OUT:
            print("매진되었습니다. 다음 기회에 이용해 주세요.")
        elif self.state is self.SOLD:
            print("알맹이를 내보내고 있습니다.")

    def ejectQuarter(self) -> None:
        if self.state is self.HAS_QUARTER:
            print("동전이 반환됩니다.")
            self.state = self.NO_QUARTER
        elif self.state is self.NO_QUARTER:
            print("동전을 넣어 주세요.")
        elif self.state is self.SOLD:
            print("이미 알맹이를 뽑으셨습니다.")
        elif self.state is self.SOLD_OUT:
            print("동전을 넣지 않으셨습니다. 동전이 반환되지 않습니다.")

    def turnCrank(self) -> None:
        if self.state is self.SOLD:
            print("손잡이는 한 번만 돌려 주세요.")
        elif self.state is self.NO_QUARTER:
            print("동전을 넣어 주세요.")
        elif self.state is self.SOLD_OUT:
            print("매진되었습니다.")
        elif self.state is self.HAS_QUARTER:
            print("손잡이를 돌리셨습니다.")
            self.state = self.SOLD
            self.dispense()

    def dispense(self) -> None:
        if self.state is self.SOLD:
            print("알맹이를 내보내고 있습니다.")
            self.count -= 1
            if self.count is 0:
                print("더 이상 알맹이가 없습니다.")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state is self.NO_QUARTER:
            print("동전을 넣어 주세요.")
        elif self.state is self.SOLD_OUT:
            print("매진입니다.")
        elif self.state is self.HAS_QUARTER:
            print("알맹이를 내보낼 수 없습니다.")

    def refill(self, numGumBalls :int) -> None:
        self.count = numGumBalls
        self.state = self.NO_QUARTER

    def __str__(self) -> str:
        result :str = ""
        result += "\n주식회사 왕뽑기"
        result += "\n파이썬으로 돌아가는 최신형 뽑기 기계\n"
        result += f"남은 개수: {self.count}개\n";
        if self.state is self.SOLD_OUT:
            result += "매진"
        elif self.state is self.NO_QUARTER:
            result += "동전 투입 대기중"
        elif self.state is self.HAS_QUARTER:
            result += "손잡이 돌리기를 대기중"
        elif self.state is self.SOLD:
            result += "알맹이 전달중"
        result += "\n"

        return result