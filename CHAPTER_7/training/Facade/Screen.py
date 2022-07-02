class Screen():
    def __init__(self, description: str) -> None:
        self.description: str = description;
    def __str__(self) -> str:
        return self.description
        
    def up(self) -> None:
        print(f"{self.description}이 올라갑니다.")

    def down(self) -> None:
        print(f"{self.description}이 내려옵니다.")
