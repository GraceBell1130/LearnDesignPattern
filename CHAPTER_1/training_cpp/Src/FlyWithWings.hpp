#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyWithWings : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("���� �־��") << std::endl;
	}
};