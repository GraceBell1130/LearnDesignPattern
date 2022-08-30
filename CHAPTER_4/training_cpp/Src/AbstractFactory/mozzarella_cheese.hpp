#pragma once
#include "../stdafx.h"
#include "cheese_interface.hpp"

namespace AbstractFactory {
	class MozzarellaCheese : public Cheese {
	public:
		std::wstring tostring() override {
			return TEXT("Shredded Mozzarella");
		};
	};
}