#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class DarkRoast : public Beverage {
public:
	DarkRoast() {
		this->description_ = TEXT("��ũ �ν�Ʈ Ŀ��");
	}

	double cost() override {
		return 0.99;
	}
};