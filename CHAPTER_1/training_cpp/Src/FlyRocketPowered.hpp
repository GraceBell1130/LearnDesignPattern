#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyRocketPowered : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("로켓 추진으로 날아갑니다.") << std::endl;
	}
};