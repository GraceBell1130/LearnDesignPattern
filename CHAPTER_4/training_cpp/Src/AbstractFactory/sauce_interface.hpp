#pragma once
#include "../stdafx.h"

namespace AbstractFactory {
	class Sauce {
	public:
		virtual std::wstring tostring() = 0;
	};
}