from pytest import *
from Facade.Screen import Screen
from Facade.PopcornPopper import PopcornPopper
from Facade.StreamingPlayer import StreamingPlayer
from Facade.Tuner import Tuner
from Facade.Projector import Projector
from Facade.Amplifier import Amplifier
from Facade.TheaterLights import TheaterLights
from Facade.HomeTheaterFacade import HomeTheaterFacade

def test_HomeTheaterFacade(capsys):
    screen: Screen = Screen("스크린")
    popper: PopcornPopper = PopcornPopper("팝콘 기계")
    amp: Amplifier = Amplifier("앰프");
    tuner: Tuner = Tuner("AM/FM 튜너");
    player: StreamingPlayer = StreamingPlayer("스트리밍 플레이어");
    projector: Projector = Projector("프로젝터");
    lights: TheaterLights = TheaterLights("조명");

    homeTheaterFacade: HomeTheaterFacade = HomeTheaterFacade(amp, tuner, player, projector, screen, lights, popper)

    homeTheaterFacade.watchMovie("인디아나 존스:레이더스")
    captured = capsys.readouterr()
    assert captured.out == '영화 볼 준비 중\n' +\
                           '팝콘 기계가 켜졌습니다.\n' +\
                           '팝콘 기계에서 팝콘을 튀기고 있습니다.\n' +\
                           '조명 밝기를 10%로 설정합니다.\n' +\
                           '스크린이 내려옵니다.\n' +\
                           '프로젝터가 켜졌습니다.\n' +\
                           '프로젝터 화면 비율을 와이드 모드로 설정합니다. (16:9 비율)\n'+\
                           '앰프가 켜졌습니다.\n' +\
                           '앰프를 스트리밍 플레이어와 연결합니다.\n' +\
                           '앰프를 서라운드 모드로 설정합니다.(5.1채널)\n' +\
                           '앰프 볼륨을 5로 설정합니다.\n' +\
                           '스트리밍 플레이어가 켜졌습니다.\n' +\
                           '스트리밍 플레이어에서 "인디아나 존스:레이더스"를 재생합니다.\n'

    homeTheaterFacade.endMovie()
    captured = capsys.readouterr()
    assert captured.out == '홈시어터를 끄는 중\n' +\
                           '팝콘 기계가 꺼졌습니다.\n' +\
                           '조명이 켜졌습니다.\n' +\
                           '스크린이 올라갑니다.\n' +\
                           '프로젝터가 꺼졌습니다.\n' +\
                           '앰프가 꺼졌습니다.\n' +\
                           '스트리밍 플레이어에서 "인디아나 존스:레이더스" 재생을 종료합니다.\n' +\
                           '스트리밍 플레이어가 꺼졌습니다.\n'
