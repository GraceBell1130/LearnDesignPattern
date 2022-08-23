#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class DarkRoast : public Beverage {
public:
	DarkRoast() {
		this->description_ = TEXT("다크 로스트 커피");
	}

	double cost() override {
		return 0.99;
	}
};