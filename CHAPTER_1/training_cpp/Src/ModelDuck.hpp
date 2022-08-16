#pragma once
#include "stdafx.h"
#include "Duck.hpp"
#include "Quack.hpp"
#include "FlyNoWay.hpp"
class ModelDuck : public Duck {
public:
	ModelDuck()
	{
		flyBehavior = std::make_unique<FlyNoWay>();
		quackBehavior = std::make_unique<Quack>();
	}

	void display()
	{
		std::wcout << TEXT("���� ���� �����Դϴ�.") << std::endl;
	}
};