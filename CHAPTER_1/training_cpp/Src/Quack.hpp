#pragma once
#include "stdafx.h"
#include "QuackBehavior.h"

class Quack : public QuackBehavior
{
public:
	void quack() override
	{
		std::wcout << TEXT("Ва") << std::endl;
	}
};