#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class HouseBlend : public Beverage {
public:
	HouseBlend() {
		this->description_ = TEXT("�Ͽ콺 ���� Ŀ��");
	}

	double cost() override {
		return 0.89;
	}
};