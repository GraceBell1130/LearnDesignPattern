#pragma once
#include "stdafx.h"
#include "command.h"
#include "stereo.hpp"

class StereoOnWithCDCommand : public Command {
public:
	StereoOnWithCDCommand(std::shared_ptr<Stereo> stereo) {
		stereo_ = stereo;
	}

	void Execute() override {
		stereo_->On();
		stereo_->SetCD();
		stereo_->SetVolume(11);
	}

	void Undo() override {
		stereo_->Off();
	}

	std::tstring Name() override {
		return TEXT("StereoOnWithCDCommand");
	}
private:
	std::shared_ptr<Stereo> stereo_;
};