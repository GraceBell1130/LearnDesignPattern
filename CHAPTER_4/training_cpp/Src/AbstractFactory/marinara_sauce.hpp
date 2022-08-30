#pragma once
#include "../stdafx.h"
#include "sauce_interface.hpp"

namespace AbstractFactory {
	class MarinaraSauce : public Sauce {
	public:
		std::wstring tostring() override {
			return TEXT("MarinaraSauce");
		};
	};
}