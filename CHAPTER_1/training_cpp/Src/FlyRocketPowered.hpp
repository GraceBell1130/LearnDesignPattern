#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"

class FlyRocketPowered : public FlyBehavior
{
public:
	void fly() override
	{
		std::wcout << TEXT("���� �������� ���ư��ϴ�.") << std::endl;
	}
};