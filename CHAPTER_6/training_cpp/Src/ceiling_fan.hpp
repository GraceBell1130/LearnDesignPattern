#pragma once
#include "stdafx.h"

class CeilingFan {
public:
	CeilingFan(std::tstring location) {
		location_ = location;
	}

	void High() {
		level_ = POWER::kHigh;
		std::tcout << location_ << TEXT(" ��ǳ�� �ӵ���  HIGH�� �����Ǿ����ϴ�.") << std::endl;
	}

	void Medium() {
		level_ = POWER::kMedium;
		std::tcout << location_ << TEXT(" ��ǳ�� �ӵ���  MEDIUM���� �����Ǿ����ϴ�.") << std::endl;
	}

	void Low() {
		level_ = POWER::kMedium;
		std::tcout << location_ << TEXT(" ��ǳ�� �ӵ���  LOW�� �����Ǿ����ϴ�.") << std::endl;
	}

	void Off() {
		level_ = POWER::kOff;
		std::tcout << location_ << TEXT(" ��ǳ�� �ӵ���  �������ϴ�.") << std::endl;
	}

	int GetSpeed() {
		return static_cast<int>(level_);
	}

private:
	std::tstring location_;
	enum class POWER {
		kOff,
		kLow,
		kMedium,
		kHigh
	};
	POWER level_;
};