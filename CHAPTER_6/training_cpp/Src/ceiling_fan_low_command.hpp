#pragma once
#include "stdafx.h"
#include "command.h"
#include "ceiling_fan.hpp"

class CeilingFanLowCommand : public Command {
public:
	CeilingFanLowCommand(std::shared_ptr<CeilingFan> ceiling_fan) {
		ceiling_fan_ = ceiling_fan;
	}

	void Execute() override {
		previous_speed_ = ceiling_fan_->GetSpeed();
		ceiling_fan_->Low();
	}

	void Undo() override {
		switch (previous_speed_)
		{
		case POWER::kHigh: {
			ceiling_fan_->High();
			break;
		}
		case POWER::kMedium: {
			ceiling_fan_->Medium();
			break;
		}
		case POWER::kLow: {
			ceiling_fan_->Low();
			break;
		}
		case POWER::kOff: {
			ceiling_fan_->Off();
			break;
		}
		}
	}

	std::tstring Name() override {
		return TEXT("CeilingFanLowCommand");
	}
private:
	std::shared_ptr<CeilingFan> ceiling_fan_;
	POWER previous_speed_;
};