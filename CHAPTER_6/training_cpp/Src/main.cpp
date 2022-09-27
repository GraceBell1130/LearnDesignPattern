#include "stdafx.h"
#include "remote_control.hpp"
#include "light.hpp"
#include "light_on_command.hpp"
#include "light_off_command.hpp"
#include "ceiling_fan.hpp"
#include "ceiling_fan_on_command.hpp"
#include "ceiling_fan_off_command.hpp"
#include "garage_door.hpp"
#include "garage_door_up_command.hpp"
#include "garage_door_down_command.hpp"
#include "stereo.hpp"
#include "stereo_on_with_cd_command.hpp"
#include "stereo_off_command.hpp"

int main() {
	std::tcout.imbue(std::locale("korean"));
	std::unique_ptr<RemoteControl> remote_control = std::make_unique<RemoteControl>();

	std::shared_ptr<Light> living_room_light = std::make_shared<Light>(TEXT("거실"));
	std::shared_ptr<Light> kitchen_light = std::make_shared<Light>(TEXT("주방"));
	std::shared_ptr<CeilingFan> ceiling_fan = std::make_shared<CeilingFan>(TEXT("거실"));
	std::shared_ptr<GarageDoor> garage_door = std::make_shared<GarageDoor>(TEXT("차고"));
	std::shared_ptr<Stereo> stereo = std::make_shared<Stereo>(TEXT("거실"));

	std::unique_ptr<LigthOnCommand> living_room_light_on = std::make_unique<LigthOnCommand>(living_room_light);
	std::unique_ptr<LigthOffCommand> living_room_light_off = std::make_unique<LigthOffCommand>(living_room_light);
	std::unique_ptr<LigthOnCommand> kitchen_light_on = std::make_unique<LigthOnCommand>(kitchen_light);
	std::unique_ptr<LigthOffCommand> kitchen_light_off = std::make_unique<LigthOffCommand>(kitchen_light);

	std::unique_ptr<CeilingFanOnCommand> ceiling_fan_on = std::make_unique<CeilingFanOnCommand>(ceiling_fan);
	std::unique_ptr<CeilingFanOffCommand> ceiling_fan_off = std::make_unique<CeilingFanOffCommand>(ceiling_fan);

	std::unique_ptr<GarageDoorUpCommand> garage_door_up = std::make_unique<GarageDoorUpCommand>(garage_door);
	std::unique_ptr<GarageDoorDownCommand> garage_door_down = std::make_unique<GarageDoorDownCommand>(garage_door);

	std::unique_ptr<StereoOnWithCDCommand> stereo_on_with_cd = std::make_unique<StereoOnWithCDCommand>(stereo);
	std::unique_ptr<StereoOffCommand> stereo_off = std::make_unique<StereoOffCommand>(stereo);

	remote_control->SetCommand(0, std::move(living_room_light_on), std::move(living_room_light_off));
	remote_control->SetCommand(1, std::move(kitchen_light_on), std::move(kitchen_light_off));
	remote_control->SetCommand(2, std::move(ceiling_fan_on), std::move(ceiling_fan_off));
	remote_control->SetCommand(3, std::move(garage_door_up), std::move(garage_door_down));
	remote_control->SetCommand(4, std::move(stereo_on_with_cd), std::move(stereo_off));

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
}