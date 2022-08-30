#pragma once
#include "stdafx.h"
class Singeton {
private:
	static std::shared_ptr<Singeton> instance;
	Singeton();
public:
	static std::shared_ptr<Singeton> getInstance() {
		if (nullptr == instance) {
			instance = std::make_unique<Singeton>();
		}
		return instance;
	}
};