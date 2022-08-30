#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleCheesePizza : public Pizza {
	public:
		NyStyleCheesePizza() {
			name = TEXT("뉴욕 스타일 소스와 치즈 피자");
			dough = TEXT("씬 크러스트 도우");
			sauce = TEXT("마리나라 소스");

			toppings.push_back(TEXT("잘게 썬 레지아노 치즈"));
		}
	};
}