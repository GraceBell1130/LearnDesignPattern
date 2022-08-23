#pragma once
#include "beverage.hpp"
#include "condiment_decorator.hpp"

class Moca : public CondimentDecorator {
public:
	Moca(std::shared_ptr<Beverage>& beverage) {
		this->beverage_ = beverage;
	}

	std::wstring getDescription() override {
		return this->beverage_->getDescription() + TEXT(", ¸ðÄ«");
	}

	double cost() override {
		return this->beverage_->cost() + 0.20;
	}
};