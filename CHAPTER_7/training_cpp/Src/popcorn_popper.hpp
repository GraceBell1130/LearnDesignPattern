#pragma once
#include "stdafx.h"

class PopcornPopper {
public:
	PopcornPopper(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void Pop() {
		std::tcout << description_ << TEXT(" popping popcorn!") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
};