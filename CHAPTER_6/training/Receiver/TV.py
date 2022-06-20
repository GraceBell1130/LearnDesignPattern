class TV():
    def __init__(self, location :str = "") -> None:
        self.location :str = location
        self.channel :int = 0 

    def on(self):
        if self.location is not "":
            print(f"{self.location} TV가 켜졌습니다.")
        else:
            print(f"TV가 켜졌습니다.")
    
    def off(self):
        if self.location is not "":
            print(f"{self.location} TV가 꺼졌습니다.")
        else:
            print(f"TV가 꺼졌습니다.")

    def setDVD(self) -> None:
        if self.location is not "":
            print(f"{self.location} TV에서 DVD를 재생합니다.")
        else:
            print(f"TV에서 DVD를 재생합니다.")

    def setInputChannel(self):
        self.channel = 3
        print(f"Channel이 VCR로 설정되었습니다.")
