#pragma once
#include "stdafx.h"
#include "command.h"
#include "stereo.hpp"

class StereoOnWithCDCommand : public Command {
public:
	StereoOnWithCDCommand(std::shared_ptr<Stereo> stereo) {
		stereo_ = stereo;
	}

	void Execute() {
		stereo_->On();
		stereo_->SetCD();
		stereo_->SetVolume(11);
	}

	std::tstring Name() {
		return TEXT("StereoOnWithCDCommand");
	}
private:
	std::shared_ptr<Stereo> stereo_;
};