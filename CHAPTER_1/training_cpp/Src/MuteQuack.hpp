#pragma once
#include "stdafx.h"
#include "QuackBehavior.h"

class MuteQuack : public QuackBehavior
{
public:
	void quack() override
	{
		std::wcout << TEXT("<< ����~ >>") << std::endl;
	}
};