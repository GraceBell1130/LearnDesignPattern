#pragma once
#include "stdafx.h"

class Beverage {
protected:
	std::wstring description_ = TEXT("���� ����");

public:
	virtual std::wstring getDescription() {
		return description_;
	}

	virtual double cost() = 0;
};