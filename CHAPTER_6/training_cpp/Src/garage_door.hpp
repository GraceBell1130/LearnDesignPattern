#pragma once
#include "stdafx.h"

class GarageDoor {
public:
	GarageDoor(std::tstring location) {
		location_ = location;
	}
	
	void Up() {
		std::tcout << location_ << TEXT(" ���� �ö󰩴ϴ�.") << std::endl;
	}

	void Down() {
		std::tcout << location_ << TEXT(" ���� �������ϴ�.") << std::endl;
	}

	void Stop() {
		std::tcout << location_ << TEXT(" ���� ������ϴ�.") << std::endl;
	}

	void LightOn() {
		std::tcout << location_ << TEXT(" ���� �������ϴ�.") << std::endl;
	}

	void LightOff() {
		std::tcout << location_ << TEXT(" ���� �������ϴ�.") << std::endl;
	}

private:
	std::tstring location_;
};