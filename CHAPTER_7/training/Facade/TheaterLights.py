class TheaterLights():
    def __init__(self, description: str) -> None:
        self.description: str = description

    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}이 켜졌습니다.")
 
    def off(self) -> None:
        print(f"{self.description}이 꺼졌습니다.")

    def dim(self, level: int) -> None:
        print(f"{self.description} 밝기를 {level}%로 설정합니다.")
