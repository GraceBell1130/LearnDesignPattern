#pragma once
#include "../stdafx.h"

namespace AbstractFactory {
	class Dough {
	public:
		virtual std::wstring tostring() = 0;
	};
}