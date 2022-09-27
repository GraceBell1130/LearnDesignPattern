#pragma once
#include "stdafx.h"
#include "command.h"
#include "ceiling_fan.hpp"

class CeilingFanOnCommand : public Command {
public:
	CeilingFanOnCommand(std::shared_ptr<CeilingFan> ceiling_fan) {
		ceiling_fan_ = ceiling_fan;
	}

	void Execute() {
		ceiling_fan_->High();
	}

	std::tstring Name() {
		return TEXT("CeilingFanOnCommand");
	}
private:
	std::shared_ptr<CeilingFan> ceiling_fan_;
};