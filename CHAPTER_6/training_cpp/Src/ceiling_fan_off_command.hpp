#pragma once
#include "stdafx.h"
#include "command.h"
#include "ceiling_fan.hpp"

class CeilingFanOffCommand : public Command {
public:
	CeilingFanOffCommand(std::shared_ptr<CeilingFan> ceiling_fan) {
		ceiling_fan_ = ceiling_fan;
	}

	void Execute() {
		ceiling_fan_->Off();
	}

	std::tstring Name() {
		return TEXT("CeilingFanOffCommand");
	}
private:
	std::shared_ptr<CeilingFan> ceiling_fan_;
};