class PopcornPopper():
    def __init__(self, description: str) -> None:
        self.description: str = description;
    
    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}가 켜졌습니다.")
 
    def off(self) -> None:
        print(f"{self.description}가 꺼졌습니다.")

    def pop(self) -> None:
        print(f"{self.description}에서 팝콘을 튀기고 있습니다.");
