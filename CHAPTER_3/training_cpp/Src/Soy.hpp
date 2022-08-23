#pragma once
#include "beverage.hpp"
#include "condiment_decorator.hpp"

class Soy: public CondimentDecorator {
public:
	Soy(std::shared_ptr<Beverage> beverage) {
		this->beverage_ = beverage;
	}

	std::wstring getDescription() override {
		return this->beverage_->getDescription() + TEXT(", µÎÀ¯");
	}

	double cost() override {
		return this->beverage_->cost() + 0.15;
	}
};