from Facade.Amplifier import Amplifier
from Facade.Tuner import Tuner
from Facade.StreamingPlayer import StreamingPlayer
from Facade.Projector import Projector
from Facade.Screen import Screen
from Facade.TheaterLights import TheaterLights
from Facade.PopcornPopper import PopcornPopper

class HomeTheaterFacade():
    def __init__(self, amp: Amplifier, tuner: Tuner, player: StreamingPlayer, 
				 projector: Projector, screen: Screen,
				 lights: TheaterLights, popper: PopcornPopper) -> None:
        self.amp: Amplifier = amp
        self.tuner: Tuner = tuner 
        self.player: StreamingPlayer = player
        self.projector: Projector = projector
        self.screen: Screen = screen
        self.lights: TheaterLights = lights
        self.popper: PopcornPopper = popper


    def watchMovie(self, movie: str) -> None:
        print("영화 볼 준비 중")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setStreamingPlayer(self.player)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.player.on()
        self.player.play(movie)


    def endMovie(self) -> None:
        print("홈시어터를 끄는 중")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()
