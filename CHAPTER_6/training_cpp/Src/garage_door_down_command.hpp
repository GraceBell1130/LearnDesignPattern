#pragma once
#include "stdafx.h"
#include "command.h"
#include "garage_door.hpp"

class GarageDoorUpCommand : public Command {
public:
	GarageDoorUpCommand(std::shared_ptr<GarageDoor> garage_door) {
		garage_door_ = garage_door;
	}

	void Execute() {
		garage_door_->Up();
	}

	std::tstring Name() {
		return TEXT("GarageDoorUpCommand");
	}
private:
	std::shared_ptr<GarageDoor> garage_door_;
};