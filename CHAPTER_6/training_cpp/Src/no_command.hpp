#pragma once
#include "command.h"

class NoCommand : public Command {
public:
	void Execute() override {

	}

	std::tstring Name() {
		return TEXT("NoCommand");
	}
};