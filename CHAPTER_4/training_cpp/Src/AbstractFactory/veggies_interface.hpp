#pragma once
#include "../stdafx.h"

namespace AbstractFactory {
	class Veggies {
	public:
		virtual std::wstring tostring() = 0;
	};
}