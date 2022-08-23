#pragma once
#include "stdafx.h"
#include "beverage.hpp"

class CondimentDecorator : public Beverage {
protected:
	std::shared_ptr<Beverage> beverage_;

public:
	virtual std::wstring getDescription() override = 0;
};
