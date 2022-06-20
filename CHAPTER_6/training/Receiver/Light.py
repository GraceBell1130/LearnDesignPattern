class Light():
    def __init__(self, location :str = "") -> None:
        self.location :str = location

    def on(self):
        if self.location is not "":
            print(f"{self.location} 조명이 켜졌습니다.")
        else:
            print(f"조명이 켜졌습니다.")
    
    def off(self):
        if self.location is not "":
            print(f"{self.location} 조명이 꺼졌습니다.")
        else:
            print(f"조명이 꺼졌습니다.")