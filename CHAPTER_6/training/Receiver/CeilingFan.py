from enum import Enum

class CeilingFan():
    class POWER(Enum):
        HIGH = 3
        MEDIUM = 2
        LOW = 1
        OFF = 0

    def __init__(self, location :str = "") -> None:
        self.location :str = location
        self.speed :self.POWER = self.POWER.OFF

    def high(self) -> None:
        self.speed :self.POWER = self.POWER.HIGH
        if self.location is not "":
            print(f"{self.location} 선풍기 속도가 HIGH로 설정되었습니다.")
        else:
            print(f"선풍기 속도가 HIGH로 설정되었습니다.")

    def medium(self) -> None:
        self.speed :self.POWER = self.POWER.MEDIUM
        if self.location is not "":
            print(f"{self.location} 선풍기 속도가 MEDIUM으로 설정되었습니다.")
        else:
            print(f"선풍기 속도가 MEDIUM로 설정되었습니다.")

    def low(self) -> None:
        self.speed :self.POWER = self.POWER.LOW
        if self.location is not "":
            print(f"{self.location} 선풍기 속도가 LOW로 설정되었습니다.")
        else:
            print(f"선풍기 속도가 LOW로 설정되었습니다.")

    def off(self) -> None:
        self.speed = 0
        if self.location is not "":
            print(f"{self.location} 선풍기가 꺼졌습니다.")
        else:
            print(f"선풍기가 꺼졌습니다.")
    
    def getSpeed(self) -> int:
        return self.speed