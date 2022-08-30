#pragma once
#include "../stdafx.h"
#include "veggies_interface.hpp"

namespace AbstractFactory {
	class BlackOlives : public Veggies {
	public:
		std::wstring tostring() override {
			return TEXT("Black Olives");
		};
	};
}