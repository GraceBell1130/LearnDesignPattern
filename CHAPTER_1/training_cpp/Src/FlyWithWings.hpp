#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyWithWings : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("날고 있어요") << std::endl;
	}
};