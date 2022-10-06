#pragma once
#include "stdafx.h"

class Screen {
public:
	Screen(std::tstring description) {
		description_ = description;
	}

	void Up() {
		std::tcout << description_ << TEXT(" going up") << std::endl;
	}

	void Down() {
		std::tcout << description_ << TEXT(" going down") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
};