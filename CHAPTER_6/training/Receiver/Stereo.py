class Stereo():
    def __init__(self, location :str = "") -> None:
        self.location = location

    def on(self) -> None:
        if self.location is not "":
            print(f"{self.location} 오디오가 켜졌습니다.")
        else:
            print(f"오디오가 켜졌습니다.")

    def off(self) -> None:
        if self.location is not "":
            print(f"{self.location} 오디오가 꺼졌습니다.")
        else:
            print(f"오디오가 꺼졌습니다.")

    def setCD(self) -> None:
        if self.location is not "":
            print(f"{self.location} 오디오에서 CD가 재생됩니다.")
        else:
            print(f"오디오에서 CD가 재생됩니다.")

    def setDVD(self) -> None:
        if self.location is not "":
            print(f"{self.location} 오디오에서 DVD가 재생됩니다.")
        else:
            print(f"오디오에서 DVD가 재생됩니다.")

    def setRadio(self) -> None:
        if self.location is not "":
            print(f"{self.location} 오디오에서 라디오가 재생됩니다.")
        else:
            print(f"오디오에서 라디오가 재생됩니다.")

    def setVolume(self, volume :int):
        if self.location is not "":
            print(f"{self.location} 오디오의 볼륨이 {volume}로 설정되었습니다.")
        else:
            print(f"오디오의 볼륨이 {volume}로 설정되었습니다.")
