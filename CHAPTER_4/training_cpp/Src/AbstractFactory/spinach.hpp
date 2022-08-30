#pragma once
#include "../stdafx.h"
#include "veggies_interface.hpp"

namespace AbstractFactory {
	class Spinach : public Veggies {
	public:
		std::wstring tostring() override {
			return TEXT("Spinach");
		};
	};
}