#pragma once
#include "stdafx.h"
#include "duck_interface.hpp"
#include "turkey_interface.hpp"

class TurkeyAdapter : public Duck {
public:
	TurkeyAdapter(std::shared_ptr<Turkey> turkey) {
		turkey_ = turkey;
	}

	void quack() {
		turkey_->gobble();
	}

	void fly() {
		for (int i = 0; i < 5; i++) {
			turkey_->fly();
		}
	}
private:
	std::shared_ptr<Turkey> turkey_;
};