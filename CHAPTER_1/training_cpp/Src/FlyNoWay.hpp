#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyNoWay : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("���� �� ���ƿ�") << std::endl;
	}
};