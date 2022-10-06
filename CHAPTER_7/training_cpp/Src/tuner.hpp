#pragma once
#include "stdafx.h"

class Tuner {
public:
	Tuner(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void SetFrequency(double frequency) {
		std::tcout << description_ << TEXT(" setting frequency to ") << frequency << std::endl;
		frequency_ = frequency;
	}

	void SetAm() {
		std::tcout << description_ << TEXT(" setting AM mode") << std::endl;
	}

	void SetPm() {
		std::tcout << description_ << TEXT(" setting FM mode") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
	double frequency_;
};