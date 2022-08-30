#pragma once
#include "../stdafx.h"
#include "dough_interface.hpp"

namespace AbstractFactory {
	class ThickCrustDough : public Dough {
	public:
		std::wstring tostring() override {
			return TEXT("ThickCrust style extra thick crust dough");
		};
	};
}