#pragma once
#include "command.h"

class MacroCommand : public Command {
public:
	MacroCommand(std::vector<std::shared_ptr<Command>> commands): commands_(commands) {

	}

	void Execute() override {
		for (std::shared_ptr<Command> command : commands_) {
			command->Execute();
		}
	}

	void Undo() override {
		std::reverse(commands_.begin(), commands_.end());
		for (std::shared_ptr<Command> command : commands_) {
			command->Undo();
		}
		std::reverse(commands_.begin(), commands_.end());
	}

	std::tstring Name() override {
		return TEXT("MacroCommand");
	}
private:
	std::vector<std::shared_ptr<Command>> commands_;
};