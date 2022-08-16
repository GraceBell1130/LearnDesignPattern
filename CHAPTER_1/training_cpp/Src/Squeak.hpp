#pragma once
#include "stdafx.h"
#include "QuackBehavior.h"

class Squeak : public QuackBehavior
{
public:
	void quack() override
	{
		std::wcout << TEXT("»à") << std::endl;
	}
};