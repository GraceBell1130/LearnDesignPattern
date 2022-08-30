#pragma once
#include "../stdafx.h"
#include "veggies_interface.hpp"

namespace AbstractFactory {
	class Garlic : public Veggies {
	public:
		std::wstring tostring() override {
			return TEXT("Garlic");
		};
	};
}