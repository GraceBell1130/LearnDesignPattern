class Hottub():
    def __init__(self) -> None:
        self.status :bool = False
        self.temperature :int = 0 

    def on(self):
       self.status = True

    def off(self):
        self.status = False

    def bubblesOn(self):
        if self.status is True:
            print("욕조가 보글보글 거리는 중입니다.")

    def bubblesOff(self):
        if self.status is False:
            print("욕조가 보글보글 거리지 않는 중입니다.")

    def jetsOn(self):
        if self.status is True:
            print("욕조 분출기가 켜졌습니다.")

    def jetsOff(self):
        if self.status is False:
            print("욕조 분출기가 꺼졌습니다.")
    
    def setTemperature(self, temperature :int):
        self.temperature = temperature
        print(f"욕조 온도를 {self.temperature}도로 설정합니다.")

    def getTemperature(self):
        print(f"현재 욕조 온도: {self.temperature}도")

    def heat(self):
        self.temperature = 105
        print("욕조가 105도로 온도가 올라가는 중입니다.")
    
    def cool(self):
        self.temperature = 98
        print("욕조가 98도로 온도가 떨어지는 중입니다.")
