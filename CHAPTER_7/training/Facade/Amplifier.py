from Facade.Tuner import Tuner
from Facade.StreamingPlayer import StreamingPlayer

class Amplifier():
    def __init__(self, description: str):
        self.description: str = description
        self.tuner: Tuner = None 
        self.player: StreamingPlayer = None 

    def __str__(self) -> str:
        return self.description

    def on(self) -> None:
        print(f"{self.description}가 켜졌습니다.")
 
    def off(self) -> None:
        print(f"{self.description}가 꺼졌습니다.")

    def setStereoSound(self) -> None:
        print(f"{self.description}를 스트레오 모드로 설정합니다.")

    def setSurroundSound(self) -> None:
        print(f"{self.description}를 서라운드 모드로 설정합니다.(5.1채널)")

    def setVolume(self, level: int) -> None:
        print(f"{self.description} 볼륨을 {level}로 설정합니다.")

    def setTuner(self, tuner: Tuner) -> None:
        print(f"{self.description}를 {tuner}로 튜너를 설정합니다.")
        self.tuner = tuner;

    def setStreamingPlayer(self, player: StreamingPlayer) -> None:
        print(f"{self.description}를 {player}와 연결합니다.")
        self.player = player