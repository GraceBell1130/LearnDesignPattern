#pragma once
#include "../stdafx.h"
#include "pepperoni_interface.hpp"

namespace AbstractFactory {
	class SlicedPepperoni : public Pepperoni {
	public:
		std::wstring tostring() override {
			return TEXT("Sliced Pepperoni");
		};
	};
}