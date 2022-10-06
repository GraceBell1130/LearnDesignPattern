#pragma once
#include "stdafx.h"
#include "duck_interface.hpp"

class MallardDuck : public Duck {
public:
	void quack() {
		std::tcout << TEXT("��") << std::endl;
	}

	void fly() {
		std::tcout << TEXT("���� �־��!") << std::endl;
	}
};