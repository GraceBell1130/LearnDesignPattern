#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class Espresso : public Beverage {
public:
	Espresso() {
		this->description_ = TEXT("����������");
	}

	double cost() override {
		return 1.99;
	}
};