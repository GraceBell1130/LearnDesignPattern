#pragma once
#include "stdafx.h"
#include "duck_interface.hpp"
#include "turkey_interface.hpp"

class DuckAdapter : public Turkey {
public:
	DuckAdapter(std::shared_ptr<Duck> duck) {
		duck_ = duck;
		std::random_device rd;
		gen_.seed(rd());
	}

	void gobble() {
		duck_->quack();
	}

	void fly() {
		std::uniform_int_distribution<int> dis(0, 5);
		if (dis(gen_) % 5 == 0) {
			duck_->fly();
		}
	}
private:
	std::shared_ptr<Duck> duck_;
	std::mt19937 gen_;
};