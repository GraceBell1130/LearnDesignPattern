#pragma once
#include "stdafx.h"

class TheaterLights {
public:
	TheaterLights(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void Dim(int level) {
		std::tcout << description_ << TEXT(" dimming to ") << level << TEXT("%") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
};