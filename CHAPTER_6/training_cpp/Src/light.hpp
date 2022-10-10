#pragma once
#include "stdafx.h"

class Light {
public:
	Light(std::tstring_view location) {
		location_ = location;
	}
	void On() {
		std::tcout << location_ << TEXT(" ������ �������ϴ�.") << std::endl;
	}
	void Off() {
		std::tcout << location_ << TEXT(" ������ �������ϴ�.") << std::endl;
	}

private:
	std::tstring location_;
};