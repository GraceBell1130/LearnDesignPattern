#pragma once
#include "../stdafx.h"
#include "clams_interface.hpp"

namespace AbstractFactory {
	class FrozenClams : public Clams {
	public:
		std::wstring tostring() override {
			return TEXT("Frozen Clams from Chesapeake Bay");
		};
	};
}