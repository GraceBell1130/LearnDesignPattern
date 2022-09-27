#pragma once
#include "stdafx.h"

class GarageDoor {
public:
	GarageDoor(std::tstring location) {
		location_ = location;
	}
	
	void Up() {
		std::tcout << location_ << TEXT(" 문이 올라갑니다.") << std::endl;
	}

	void Down() {
		std::tcout << location_ << TEXT(" 문이 내려갑니다.") << std::endl;
	}

	void Stop() {
		std::tcout << location_ << TEXT(" 문이 멈췄습니다.") << std::endl;
	}

	void LightOn() {
		std::tcout << location_ << TEXT(" 불이 켜졌습니다.") << std::endl;
	}

	void LightOff() {
		std::tcout << location_ << TEXT(" 불이 꺼졌습니다.") << std::endl;
	}

private:
	std::tstring location_;
};