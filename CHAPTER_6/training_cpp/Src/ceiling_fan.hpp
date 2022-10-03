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

	POWER GetSpeed() {
		return level_;
	}

private:
	std::tstring location_;
	POWER level_;
};