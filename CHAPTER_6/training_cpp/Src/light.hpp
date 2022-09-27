#pragma once
#include "stdafx.h"

class Light {
public:
	Light(std::tstring_view location) {
		location_ = location;
	}
	void on() {
		std::tcout << location_ << TEXT(" 조명이 켜졌습니다.") << std::endl;
	}
	void off() {
		std::tcout << location_ << TEXT(" 조명이 꺼졌습니다.") << std::endl;
	}

private:
	std::tstring location_;
};