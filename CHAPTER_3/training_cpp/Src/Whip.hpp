#pragma once
#include "beverage.hpp"
#include "condiment_decorator.hpp"

class Whip : public CondimentDecorator {
public:
	Whip(std::shared_ptr<Beverage> beverage) {
		this->beverage_ = beverage;
	}

	std::wstring getDescription() override {
		return this->beverage_->getDescription() + TEXT(", ÈÖÇÎÅ©¸²");
	}

	double cost() override {
		return this->beverage_->cost() + 0.10;
	}
};