#pragma once
#include "stdafx.h"
#include "FlyBehavior.h"
#include "QuackBehavior.h"

class Duck 
{
public:
	std::unique_ptr<FlyBehavior> flyBehavior;
	std::unique_ptr<QuackBehavior> quackBehavior;

	Duck() = default;

	virtual void display(){};

	void performFly()
	{
		flyBehavior->fly();
	}
	void performQuack()
	{
		quackBehavior->quack();
	}
	void swim()
	{
		std::wcout << TEXT("��� ������ ���� ��ϴ�. ��¥ ������ ����") << std::endl;
	}
	void setFlyBehavior(std::unique_ptr<FlyBehavior> fb)
	{
		flyBehavior = std::move(fb);
	}
	void setQuackBehavior(std::unique_ptr<QuackBehavior> qb)
	{
		quackBehavior = std::move(qb);
	}
};