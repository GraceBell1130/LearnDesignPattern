#pragma once
#include "../stdafx.h"

namespace AbstractFactory {
	class Cheese {
	public:
		virtual std::wstring tostring() = 0;
	};
}