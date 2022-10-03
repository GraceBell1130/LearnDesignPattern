#pragma once
#include "stdafx.h"
#include "command.h"
#include "garage_door.hpp"

class GarageDoorDownCommand : public Command {
public:
	GarageDoorDownCommand(std::shared_ptr<GarageDoor> garage_door) {
		garage_door_ = garage_door;
	}

	void Execute() override {
		garage_door_->Down();
	}

	void Undo() override {
		garage_door_->Up();
	}

	std::tstring Name() override {
		return TEXT("GarageDoorDownCommand");
	}
private:
	std::shared_ptr<GarageDoor> garage_door_;
};