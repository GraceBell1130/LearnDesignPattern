#pragma once
#include "stdafx.h"
#include "command.h"
#include "light.hpp"

class LigthOffCommand : public Command {
public:
	LigthOffCommand(std::shared_ptr<Light> light) {
		light_ = light;
	}
	void Execute() {
		light_->off();
	}
	
	std::tstring Name() {
		return TEXT("LigthOffCommand");
	}

private:
	std::shared_ptr<Light> light_;
};