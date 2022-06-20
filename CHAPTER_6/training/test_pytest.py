from pytest import *
from Receiver.Light import Light
from Receiver.GarageDoor import GarageDoor
from Receiver.CeilingFan import CeilingFan
from Receiver.Stereo import Stereo
from Commander.LightCommand import LightOnCommand, LightOffCommand
from Commander.GarageDoorCommand import GarageDoorOpenCommand, GarageDoorUpCommand, GarageDoorDownCommand
from Commander.CeilingFanCommand import CeilingFanOnCommand, CeilingFanOffCommand
from Commander.StereoCommand import StereoOnWithCDCommand, StereoOffCommand
from Invoker.SimpleReomoteControl import SimpleRemoteControl
from Invoker.RemoteControl import RemoteControl

def test_LightRemoteControl(capsys):
    remote = SimpleRemoteControl()
    light = Light()
    lightOn = LightOnCommand(light)

    remote.setCommand(lightOn)
    remote.buttonWasPressed()
    captured = capsys.readouterr()
    assert captured.out == "조명이 켜졌습니다.\n"

def test_GarageRemoteControl(capsys):
    remote = SimpleRemoteControl()
    garageDoor = GarageDoor()
    garageOpen = GarageDoorOpenCommand(garageDoor)

    remote.setCommand(garageOpen)
    remote.buttonWasPressed()
    captured = capsys.readouterr()
    assert captured.out == "차고 문이 올라갑니다.\n"

def test_RemoteLoader(capsys):
    remoteControl :RemoteControl = RemoteControl()

    livingRoomLight :Light = Light("거실") 
    kitchenLight :Light = Light("주방") 
    ceilingFan :CeilingFan = CeilingFan("거실")
    garageDoor :GarageDoor = GarageDoor("주차장")
    stereo :Stereo = Stereo("거실")

    livingRoomLightOn :LightOnCommand = LightOnCommand(livingRoomLight)
    livingRoomLightOff :LightOffCommand = LightOffCommand(livingRoomLight)
    kitchenLightOn :LightOnCommand = LightOnCommand(kitchenLight)
    kitchenLightOff :LightOffCommand = LightOffCommand(kitchenLight)

    ceilingFanOn :CeilingFanOnCommand = CeilingFanOnCommand(ceilingFan)
    ceilingFanOff :CeilingFanOffCommand = CeilingFanOffCommand(ceilingFan)

    garageDoorUp : GarageDoorUpCommand = GarageDoorUpCommand(garageDoor)
    garageDoorDown : GarageDoorDownCommand = GarageDoorDownCommand(garageDoor)

    stereoOnWithCD :StereoOnWithCDCommand = StereoOnWithCDCommand(stereo)
    stereoOff :StereoOffCommand = StereoOffCommand(stereo)

    remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
    remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff)
    remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff)
    remoteControl.setCommand(3, stereoOnWithCD, stereoOff)

    print(remoteControl)
    captured = capsys.readouterr()

    assert captured.out == '\n----- 리모컨 -----\n' +\
                            '[slot 0] LightOnCommand LightOffCommand\n' +\
                            '[slot 1] LightOnCommand LightOffCommand\n' +\
                            '[slot 2] CeilingFanOnCommand CeilingFanOffCommand\n' +\
                            '[slot 3] StereoOnWithCDCommand StereoOffCommand\n' +\
                            '[slot 4] NoCommand NoCommand\n' +\
                            '[slot 5] NoCommand NoCommand\n' +\
                            '[slot 6] NoCommand NoCommand\n' +\
                            '[undo] NoCommand\n\n'


    remoteControl.onButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == "거실 조명이 켜졌습니다.\n"

    remoteControl.offButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == "거실 조명이 꺼졌습니다.\n"

    remoteControl.onButtonWasPushed(1)
    captured = capsys.readouterr()
    assert captured.out == "주방 조명이 켜졌습니다.\n"

    remoteControl.offButtonWasPushed(1)
    captured = capsys.readouterr()
    assert captured.out == "주방 조명이 꺼졌습니다.\n"

    remoteControl.onButtonWasPushed(2)
    captured = capsys.readouterr()
    assert captured.out == '거실 선풍기 속도가 HIGH로 설정되었습니다.\n'

    remoteControl.offButtonWasPushed(2)
    captured = capsys.readouterr()
    assert captured.out == "거실 선풍기가 꺼졌습니다.\n"

    remoteControl.onButtonWasPushed(3)
    captured = capsys.readouterr()
    assert captured.out == '거실 오디오가 켜졌습니다.\n'+\
                           '거실 오디오에서 CD가 재생됩니다.\n'+\
                           '거실 오디오의 볼륨이 11로 설정되었습니다.\n'

    remoteControl.offButtonWasPushed(3)
    captured = capsys.readouterr()
    assert captured.out == "거실 오디오가 꺼졌습니다.\n"



def test_RemoteUndoLoader(capsys):
    remoteControl :RemoteControl = RemoteControl()
    
    livingRoomLight :Light = Light("거실") 
    
    livingRoomLightOn :LightOnCommand = LightOnCommand(livingRoomLight)
    livingRoomLightOff :LightOffCommand = LightOffCommand(livingRoomLight)

    remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)

    remoteControl.onButtonWasPushed(0)
    remoteControl.offButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == '거실 조명이 켜졌습니다.\n' +\
                           '거실 조명이 꺼졌습니다.\n'
    print(remoteControl)
    captured = capsys.readouterr()
    assert captured.out == '\n----- 리모컨 -----\n' +\
                            '[slot 0] LightOnCommand LightOffCommand\n' +\
                            '[slot 1] NoCommand NoCommand\n' +\
                            '[slot 2] NoCommand NoCommand\n' +\
                            '[slot 3] NoCommand NoCommand\n' +\
                            '[slot 4] NoCommand NoCommand\n' +\
                            '[slot 5] NoCommand NoCommand\n' +\
                            '[slot 6] NoCommand NoCommand\n' +\
                            '[undo] LightOffCommand\n\n'

    remoteControl.undoButtonWasPushed()
    remoteControl.offButtonWasPushed(0)
    remoteControl.onButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == '거실 조명이 켜졌습니다.\n' +\
                           '거실 조명이 꺼졌습니다.\n' +\
                           '거실 조명이 켜졌습니다.\n'

    print(remoteControl)
    captured = capsys.readouterr()
    assert captured.out == '\n----- 리모컨 -----\n' +\
                            '[slot 0] LightOnCommand LightOffCommand\n' +\
                            '[slot 1] NoCommand NoCommand\n' +\
                            '[slot 2] NoCommand NoCommand\n' +\
                            '[slot 3] NoCommand NoCommand\n' +\
                            '[slot 4] NoCommand NoCommand\n' +\
                            '[slot 5] NoCommand NoCommand\n' +\
                            '[slot 6] NoCommand NoCommand\n' +\
                            '[undo] LightOnCommand\n\n'

    remoteControl.undoButtonWasPushed()
    captured = capsys.readouterr()
    assert captured.out == '거실 조명이 꺼졌습니다.\n'

from Commander.CeilingFanCommand import CeilingFanHighCommand, CeilingFanMediumCommand

def test_CeilingFan(capsys):
    remoteControl :RemoteControl = RemoteControl()
    ceilingFan :CeilingFan = CeilingFan("거실")

    ceilingFanMedium :CeilingFanMediumCommand = CeilingFanMediumCommand(ceilingFan)
    ceilingFanHigh :CeilingFanHighCommand = CeilingFanHighCommand(ceilingFan)
    ceilingFanOff :CeilingFanOffCommand = CeilingFanOffCommand(ceilingFan)

    remoteControl.setCommand(0, ceilingFanMedium, ceilingFanOff)
    remoteControl.setCommand(1, ceilingFanHigh, ceilingFanOff)

    remoteControl.onButtonWasPushed(0)
    remoteControl.offButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == '거실 선풍기 속도가 MEDIUM으로 설정되었습니다.\n' +\
                           '거실 선풍기가 꺼졌습니다.\n'


    print(remoteControl)
    captured = capsys.readouterr()
    assert captured.out == '\n----- 리모컨 -----\n' +\
                            '[slot 0] CeilingFanMediumCommand CeilingFanOffCommand\n' +\
                            '[slot 1] CeilingFanHighCommand CeilingFanOffCommand\n' +\
                            '[slot 2] NoCommand NoCommand\n' +\
                            '[slot 3] NoCommand NoCommand\n' +\
                            '[slot 4] NoCommand NoCommand\n' +\
                            '[slot 5] NoCommand NoCommand\n' +\
                            '[slot 6] NoCommand NoCommand\n' +\
                            '[undo] CeilingFanOffCommand\n\n'

    remoteControl.undoButtonWasPushed()
    remoteControl.onButtonWasPushed(1)
    captured = capsys.readouterr()
    assert captured.out == '거실 선풍기 속도가 MEDIUM으로 설정되었습니다.\n' +\
                           '거실 선풍기 속도가 HIGH로 설정되었습니다.\n'
    print(remoteControl)
    captured = capsys.readouterr()
    assert captured.out == '\n----- 리모컨 -----\n' +\
                            '[slot 0] CeilingFanMediumCommand CeilingFanOffCommand\n' +\
                            '[slot 1] CeilingFanHighCommand CeilingFanOffCommand\n' +\
                            '[slot 2] NoCommand NoCommand\n' +\
                            '[slot 3] NoCommand NoCommand\n' +\
                            '[slot 4] NoCommand NoCommand\n' +\
                            '[slot 5] NoCommand NoCommand\n' +\
                            '[slot 6] NoCommand NoCommand\n' +\
                            '[undo] CeilingFanHighCommand\n\n'

    remoteControl.undoButtonWasPushed()
    captured = capsys.readouterr()
    assert captured.out == '거실 선풍기 속도가 MEDIUM으로 설정되었습니다.\n'

from Receiver.TV import TV
from Receiver.Hottub import Hottub
from Commander.StereoCommand import StereoOnCommand, StereoOffCommand
from Commander.TVCommand import TvOnCommand, TvOffCommand
from Commander.HottubCommand import HottubOnCommand, HottubOffCommand
from Commander.Command import MacroCommand

def test_MacroCommand(capsys):
    light :Light = Light("거실") 
    tv :TV = TV("거실") 
    hottub :Hottub = Hottub()

    lightOn :LightOnCommand = LightOnCommand(light)
    tvOn :TvOnCommand = TvOnCommand(tv)
    hottubOn :HottubOnCommand = HottubOnCommand(hottub)

    lightOff :LightOffCommand = LightOffCommand(light)
    tvOff :TvOffCommand = TvOffCommand(tv)
    hottubOff :HottubOffCommand = HottubOffCommand(hottub)

    partyOn = [lightOn, tvOn, hottubOn]
    partyOff = [lightOff, tvOff, hottubOff]

    partyOnMacro = MacroCommand(partyOn)
    partyOffMacro = MacroCommand(partyOff)

    remoteControl :RemoteControl = RemoteControl()
    remoteControl.setCommand(0, partyOnMacro, partyOffMacro)

    print(remoteControl)
    captured = capsys.readouterr()
    assert captured.out == '\n----- 리모컨 -----\n' +\
                        '[slot 0] MacroCommand MacroCommand\n' +\
                        '[slot 1] NoCommand NoCommand\n' +\
                        '[slot 2] NoCommand NoCommand\n' +\
                        '[slot 3] NoCommand NoCommand\n' +\
                        '[slot 4] NoCommand NoCommand\n' +\
                        '[slot 5] NoCommand NoCommand\n' +\
                        '[slot 6] NoCommand NoCommand\n' +\
                        '[undo] NoCommand\n\n'

    print("--- 매크로 ON ---")
    remoteControl.onButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == '--- 매크로 ON ---\n' +\
                           '거실 조명이 켜졌습니다.\n' +\
                           '거실 TV가 켜졌습니다.\n' +\
                           '거실 TV에서 DVD를 재생합니다.\n' +\
                           '욕조 온도를 40도로 설정합니다.\n' +\
                           '현재 욕조 온도: 40도\n'

    print("--- 매크로 OFF ---")
    remoteControl.offButtonWasPushed(0)
    captured = capsys.readouterr()
    assert captured.out == '--- 매크로 OFF ---\n' +\
                           '거실 조명이 꺼졌습니다.\n' +\
                           '거실 TV가 꺼졌습니다.\n' +\
                           '욕조 온도를 36도로 설정합니다.\n'
