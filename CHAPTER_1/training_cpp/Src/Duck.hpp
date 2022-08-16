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
		std::wcout << TEXT("모든 오리는 물에 뜹니다. 가짜 오리도 뜨죠") << std::endl;
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