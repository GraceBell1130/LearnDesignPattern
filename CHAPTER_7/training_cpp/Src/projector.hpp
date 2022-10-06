#pragma once
#include "stdafx.h"

class Projector {
public:
	Projector(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void WideScreenMode() {
		std::tcout << description_ << TEXT(" in widescreen mode (16x9 aspect ratio)") << std::endl;
	}

	void TvMode() {
		std::tcout << description_ << TEXT(" in tv mode (4x3 aspect ratio)") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
};