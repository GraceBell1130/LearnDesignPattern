#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleVeggiePizza : public Pizza {
	public:
		NyStyleVeggiePizza() {
			name = TEXT("뉴욕 스타일 야채 피자");
			dough = TEXT("씬 크러스트 도우");
			sauce = TEXT("마리나라 소스");

			toppings.push_back(TEXT("잘게 썬 레지아노 치즈"));
			toppings.push_back(TEXT("마늘"));
			toppings.push_back(TEXT("양파"));
			toppings.push_back(TEXT("버섯"));
			toppings.push_back(TEXT("고추"));
		}
	};
}