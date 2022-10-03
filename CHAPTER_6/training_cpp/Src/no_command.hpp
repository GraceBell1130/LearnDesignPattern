#pragma once
#include "command.h"

class NoCommand : public Command {
public:
	void Execute() override {
	}

	void Undo() override {
	}

	std::tstring Name() override {
		return TEXT("NoCommand");
	}
};