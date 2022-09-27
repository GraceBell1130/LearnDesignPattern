#pragma once
#include "stdafx.h"
#include "command.h"
#include "no_command.hpp"
class RemoteControl {
public:
	RemoteControl() {
		for (int i = 0; i < kCommandSize; i++) {
			on_commands.push_back(std::make_unique<NoCommand>());
			off_commands.push_back(std::make_unique<NoCommand>());
		}
	}

	void SetCommand(uint8_t slot, std::unique_ptr<Command> on_command, std::unique_ptr<Command> off_command) {
		on_commands.at(slot) = std::move(on_command);
		off_commands.at(slot) = std::move(off_command);
	}

	void OnButtonWasPushed(uint8_t slot) {
		on_commands.at(slot)->Execute();
	}

	void OffButtonWasPushed(uint8_t slot) {
		off_commands.at(slot)->Execute();
	}

	std::tstring toString() {
		std::tstringstream buffer;
		buffer << TEXT("\n----- ¸®¸ðÄÁ -----\n");
		for (uint8_t i = 0; i < kCommandSize; i++) {
			buffer << TEXT("[slot ") << i << TEXT("]") << on_commands.at(i)->Name() << TEXT("\t") << off_commands.at(i)->Name() << std::endl;
		}
		return buffer.str();
	}

private:
	std::vector<std::unique_ptr<Command>> on_commands;
	std::vector<std::unique_ptr<Command>> off_commands;
	const uint8_t kCommandSize = 7;
};