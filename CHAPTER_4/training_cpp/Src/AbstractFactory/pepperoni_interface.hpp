#pragma once
#include "../stdafx.h"

namespace AbstractFactory {
	class Pepperoni {
	public:
		virtual std::wstring tostring() = 0;
	};
}