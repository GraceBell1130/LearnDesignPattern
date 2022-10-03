#pragma once
#include "stdafx.h"
#include "command.h"
#include "no_command.hpp"

class RemoteControl {
public:
	RemoteControl() {
		for (int i = 0; i < kCommandSize_; i++) {
			on_commands_.push_back(std::make_shared<NoCommand>());
			off_commands_.push_back(std::make_shared<NoCommand>());
		}
		undo_command_ = std::make_shared<NoCommand>();
	}

	void SetCommand(uint8_t slot, std::shared_ptr<Command> on_command, std::shared_ptr<Command> off_command) {
		on_commands_.at(slot) = on_command;
		off_commands_.at(slot) = off_command;
	}

	void OnButtonWasPushed(uint8_t slot) {
		on_commands_.at(slot)->Execute();
		undo_command_ = on_commands_.at(slot);
	}

	void OffButtonWasPushed(uint8_t slot) {
		off_commands_.at(slot)->Execute();
		undo_command_ = off_commands_.at(slot);
	}

	void undoButtonWasPushed() {
		undo_command_->Undo();
	}

	std::tstring toString() {
		std::tstringstream buffer;
		buffer << TEXT("\n----- ¸®¸ðÄÁ -----\n");
		for (uint8_t i = 0; i < kCommandSize_; i++) {
			buffer << TEXT("[slot ") << i << TEXT("]") << on_commands_.at(i)->Name() << TEXT("\t") << off_commands_.at(i)->Name() << std::endl;
		}
		buffer << TEXT("[undo]") << undo_command_->Name() << std::endl;
		return buffer.str();
	}

private:
	std::vector<std::shared_ptr<Command>> on_commands_;
	std::vector<std::shared_ptr<Command>> off_commands_;
	std::shared_ptr<Command> undo_command_;
	const uint8_t kCommandSize_ = 7;
};