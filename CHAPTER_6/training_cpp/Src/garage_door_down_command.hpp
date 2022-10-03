#pragma once
#include "stdafx.h"
#include "command.h"
#include "garage_door.hpp"

class GarageDoorUpCommand : public Command {
public:
	GarageDoorUpCommand(std::shared_ptr<GarageDoor> garage_door) {
		garage_door_ = garage_door;
	}

	void Execute() override {
		garage_door_->Up();
	}

	void Undo() override {
		garage_door_->Down();
	}

	std::tstring Name() override {
		return TEXT("GarageDoorUpCommand");
	}
private:
	std::shared_ptr<GarageDoor> garage_door_;
};