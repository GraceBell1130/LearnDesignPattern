#pragma once
#include "stdafx.h"

enum class POWER {
	kOff,
	kLow,
	kMedium,
	kHigh
};

class CeilingFan {
public:
	CeilingFan(std::tstring location) {
		location_ = location;
	}

	void High() {
		level_ = POWER::kHigh;
		std::tcout << location_ << TEXT(" 선풍기 속도가  HIGH로 설정되었습니다.") << std::endl;
	}

	void Medium() {
		level_ = POWER::kMedium;
		std::tcout << location_ << TEXT(" 선풍기 속도가  MEDIUM으로 설정되었습니다.") << std::endl;
	}

	void Low() {
		level_ = POWER::kMedium;
		std::tcout << location_ << TEXT(" 선풍기 속도가  LOW로 설정되었습니다.") << std::endl;
	}

	void Off() {
		level_ = POWER::kOff;
		std::tcout << location_ << TEXT(" 선풍기 속도가  꺼졌습니다.") << std::endl;
	}

	POWER GetSpeed() {
		return level_;
	}

private:
	std::tstring location_;
	POWER level_;
};