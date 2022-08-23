#pragma once
#include "stdafx.h"

class Beverage {
protected:
	std::wstring description_ = TEXT("제목 없음");

public:
	virtual std::wstring getDescription() {
		return description_;
	}

	virtual double cost() = 0;
};