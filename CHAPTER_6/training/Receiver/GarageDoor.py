class GarageDoor():
    def __init__(self, location :str = "") -> None:
        self.location :str = location

    def up(self):
        if self.location is not "":
            print(f"{self.location} 차고 문이 올라갑니다.")
        else:
            print(f"차고 문이 올라갑니다.")
    
    def down(self):
        if self.location is not "":
            print(f"{self.location} 차고 문이 내려갑니다.")
        else:
            print(f"차고 문이 내려갑니다.")
    
    def stop(self):
        if self.location is not "":
            print(f"{self.location} 차고 문이 멈췄습니다.")
        else:
            print(f"차고 문이 멈췄습니다.")
    
    def lightOn(self):
        if self.location is not "":
            print(f"{self.location} 차고 조명이 켜졌습니다.")
        else:
            print(f"차고 조명이 켜졌습니다.")
        
    def lightOff(self):
        if self.location is not "":
            print(f"{self.location} 차고 조명이 꺼졌습니다.")
        else:
            print(f"차고 조명이 꺼졌습니다.")