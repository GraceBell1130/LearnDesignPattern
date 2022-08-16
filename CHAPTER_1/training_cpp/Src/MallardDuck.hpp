#pragma once
#include "stdafx.h"
#include "Duck.hpp"
#include "Quack.hpp"
#include "FlyWithWings.hpp"
class MallardDuck : public Duck {
public:
	MallardDuck()
	{
		flyBehavior = std::make_unique<FlyWithWings>();
		quackBehavior = std::make_unique<Quack>();
	}

	void display()
	{
		std::wcout << TEXT("저는 물오리입니다.") << std::endl;
	}
};