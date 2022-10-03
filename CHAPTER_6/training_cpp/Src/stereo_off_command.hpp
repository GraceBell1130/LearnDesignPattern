#pragma once
#include "stdafx.h"
#include "command.h"
#include "stereo.hpp"

class StereoOffCommand : public Command {
public:
	StereoOffCommand(std::shared_ptr<Stereo> stereo) {
		stereo_ = stereo;
	}

	void Execute() override {
		stereo_->Off();
	}

	void Undo() override {
		stereo_->On();
	}

	std::tstring Name() override {
		return TEXT("StereoOffCommand");
	}
private:
	std::shared_ptr<Stereo> stereo_;
};