#pragma once
#include "../stdafx.h"
#include "sauce_interface.hpp"

namespace AbstractFactory {
	class PlumTomatoSauce : public Sauce {
	public:
		std::wstring tostring() override {
			return TEXT("Tomato sauce with plum tomatoes");
		};
	};
}