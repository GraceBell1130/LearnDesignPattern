#pragma once
#include "../stdafx.h"
#include "cheese_interface.hpp"

namespace AbstractFactory {
	class ReggianoCheese : public Cheese {
	public:
		std::wstring tostring() override {
			return TEXT("Reggiano Cheese");
		};
	};
}