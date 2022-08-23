#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class Espresso : public Beverage {
public:
	Espresso() {
		this->description_ = TEXT("에스프레소");
	}

	double cost() override {
		return 1.99;
	}
};