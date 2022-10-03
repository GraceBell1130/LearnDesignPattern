#include "stdafx.h"
#include "remote_control.hpp"
#include "light.hpp"
#include "light_on_command.hpp"
#include "light_off_command.hpp"
#include "ceiling_fan.hpp"
#include "ceiling_fan_on_command.hpp"
#include "ceiling_fan_off_command.hpp"
#include "ceiling_fan_high_command.hpp"
#include "ceiling_fan_medium_command.hpp"
#include "ceiling_fan_low_command.hpp"
#include "garage_door.hpp"
#include "garage_door_up_command.hpp"
#include "garage_door_down_command.hpp"
#include "stereo.hpp"
#include "stereo_on_with_cd_command.hpp"
#include "stereo_off_command.hpp"
#include "macro_command.hpp"

int main() {
	std::tcout.imbue(std::locale("korean"));
	std::unique_ptr<RemoteControl> remote_control = std::make_unique<RemoteControl>();

	std::shared_ptr<Light> living_room_light = std::make_shared<Light>(TEXT("거실"));
	std::shared_ptr<Light> kitchen_light = std::make_shared<Light>(TEXT("주방"));
	std::shared_ptr<CeilingFan> ceiling_fan = std::make_shared<CeilingFan>(TEXT("거실"));
	std::shared_ptr<GarageDoor> garage_door = std::make_shared<GarageDoor>(TEXT("차고"));
	std::shared_ptr<Stereo> stereo = std::make_shared<Stereo>(TEXT("거실"));

	std::shared_ptr<LigthOnCommand> living_room_light_on = std::make_shared<LigthOnCommand>(living_room_light);
	std::shared_ptr<LigthOffCommand> living_room_light_off = std::make_shared<LigthOffCommand>(living_room_light);
	std::shared_ptr<LigthOnCommand> kitchen_light_on = std::make_shared<LigthOnCommand>(kitchen_light);
	std::shared_ptr<LigthOffCommand> kitchen_light_off = std::make_shared<LigthOffCommand>(kitchen_light);

	std::shared_ptr<CeilingFanOnCommand> ceiling_fan_on = std::make_shared<CeilingFanOnCommand>(ceiling_fan);
	std::shared_ptr<CeilingFanOffCommand> ceiling_fan_off = std::make_shared<CeilingFanOffCommand>(ceiling_fan);

	std::shared_ptr<GarageDoorUpCommand> garage_door_up = std::make_shared<GarageDoorUpCommand>(garage_door);
	std::shared_ptr<GarageDoorDownCommand> garage_door_down = std::make_shared<GarageDoorDownCommand>(garage_door);

	std::shared_ptr<StereoOnWithCDCommand> stereo_on_with_cd = std::make_shared<StereoOnWithCDCommand>(stereo);
	std::shared_ptr<StereoOffCommand> stereo_off = std::make_shared<StereoOffCommand>(stereo);

	remote_control->SetCommand(0, living_room_light_on, living_room_light_off);
	remote_control->SetCommand(1, kitchen_light_on, kitchen_light_off);
	remote_control->SetCommand(2, ceiling_fan_on, ceiling_fan_off);
	remote_control->SetCommand(3, garage_door_up, garage_door_down);
	remote_control->SetCommand(4, stereo_on_with_cd, stereo_off);

	std::tcout << remote_control->toString() << std::endl;

	remote_control->OnButtonWasPushed(0);
	remote_control->OffButtonWasPushed(0);
	remote_control->OnButtonWasPushed(1);
	remote_control->OffButtonWasPushed(1);
	remote_control->OnButtonWasPushed(2);
	remote_control->OffButtonWasPushed(2);
	remote_control->OnButtonWasPushed(3);
	remote_control->OffButtonWasPushed(3);
	remote_control->OnButtonWasPushed(4);
	remote_control->OffButtonWasPushed(4);

	std::tcout << std::endl;
	remote_control->OnButtonWasPushed(0);
	remote_control->OffButtonWasPushed(0);

	std::tcout << remote_control->toString() << std::endl;
	remote_control->undoButtonWasPushed();
	remote_control->OffButtonWasPushed(0);
	remote_control->OnButtonWasPushed(0);
	
	std::tcout << remote_control->toString() << std::endl;
	remote_control->undoButtonWasPushed();

	std::tcout << std::endl;
	std::shared_ptr<CeilingFanMediumCommand> ceiling_fan_medium = std::make_shared<CeilingFanMediumCommand>(ceiling_fan);
	std::shared_ptr<CeilingFanHighCommand> ceiling_fan_hgih = std::make_shared<CeilingFanHighCommand>(ceiling_fan);
	remote_control->SetCommand(0, ceiling_fan_medium, ceiling_fan_off);
	remote_control->SetCommand(1, ceiling_fan_hgih, ceiling_fan_off);

	remote_control->OnButtonWasPushed(0);
	remote_control->OffButtonWasPushed(0);
	std::tcout << remote_control->toString() << std::endl;
	remote_control->undoButtonWasPushed();

	remote_control->OnButtonWasPushed(1);
	std::tcout << remote_control->toString() << std::endl;
	remote_control->undoButtonWasPushed();

	std::vector<std::shared_ptr<Command>> party_on = {living_room_light_on, kitchen_light_on, ceiling_fan_on, garage_door_up, stereo_on_with_cd};
	std::vector<std::shared_ptr<Command>> party_off = { living_room_light_off , kitchen_light_off, ceiling_fan_off, garage_door_down, stereo_off};

	std::shared_ptr<MacroCommand> party_on_macro = std::make_shared<MacroCommand>(party_on);
	std::shared_ptr<MacroCommand> party_off_macro = std::make_shared<MacroCommand>(party_off);

	remote_control->SetCommand(0, party_on_macro, party_off_macro);
	std::tcout << remote_control->toString() << std::endl;
	std::tcout << TEXT("--- 매크로 ON ---") << std::endl;
	remote_control->OnButtonWasPushed(0);
	std::tcout << TEXT("--- 매크로 OFF ---") << std::endl;
	remote_control->OffButtonWasPushed(0);
	std::tcout << TEXT("--- Undo ---") << std::endl;
	remote_control->undoButtonWasPushed();
}