#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class HouseBlend : public Beverage {
public:
	HouseBlend() {
		this->description_ = TEXT("하우스 블렌드 커피");
	}

	double cost() override {
		return 0.89;
	}
};