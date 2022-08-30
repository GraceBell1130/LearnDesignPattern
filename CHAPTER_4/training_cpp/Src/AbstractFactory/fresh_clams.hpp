#pragma once
#include "../stdafx.h"
#include "clams_interface.hpp"

namespace AbstractFactory {
	class FreshClams : public Clams {
	public:
		std::wstring tostring() override {
			return TEXT("Fresh Clams from Long Island Sound");
		};
	};
}