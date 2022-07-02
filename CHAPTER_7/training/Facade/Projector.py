class Projector():
    def __init__(self, description: str) -> None:
        self.description = description;

    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}가 켜졌습니다.")
 
    def off(self) -> None:
        print(f"{self.description}가 꺼졌습니다.")

    def wideScreenMode(self) -> None:
        print(f"{self.description} 화면 비율을 와이드 모드로 설정합니다. (16:9 비율)")

    def tvMode(self) -> None:
        print(f"{self.description} 화면 비율을 티비 모드로 설정합니다. (4:3 비율)")
