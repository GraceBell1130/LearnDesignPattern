#pragma once
#include "stdafx.h"
#include "duck_interface.hpp"

class MallardDuck : public Duck {
public:
	void quack() {
		std::tcout << TEXT("꽥") << std::endl;
	}

	void fly() {
		std::tcout << TEXT("날고 있어요!") << std::endl;
	}
};