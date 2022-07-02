class Tuner():
    def __init__(self, description: str) -> None:
        self.description :str = description
        self.frequency :float = 0.0
        
    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}가 켜졌습니다.")

    def off(self) -> None:
        print(f"{self.description}가 꺼졌습니다.")

    def setFrequency(self, frequency: float) -> None:
        print(f"{self.description}를 {frequency}로 설정했습니다.")
        self.frequency = frequency;

    def setAm(self) -> None:
        print(f"{self.description}를 AM모드로 설정했습니다.")

    def setFm(self) -> None:
        print(f"{self.description}를 FM모드로 설정했습니다.")
