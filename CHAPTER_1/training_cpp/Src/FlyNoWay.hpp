#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyNoWay : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("저는 못 날아요") << std::endl;
	}
};