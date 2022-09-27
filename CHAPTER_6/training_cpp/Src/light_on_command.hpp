#pragma once
#include "stdafx.h"
#include "command.h"
#include "light.hpp"

class LigthOnCommand : public Command {
public:
	LigthOnCommand(std::shared_ptr<Light> light) {
		light_ = light;
	}
	void Execute() {
		light_->on();
	}
	std::tstring Name() {
		return TEXT("LigthOnCommand");
	}

private:
	std::shared_ptr<Light> light_;
};