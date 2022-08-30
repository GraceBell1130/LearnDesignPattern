#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleClamPizza : public Pizza {
	public:
		NyStyleClamPizza() {
			name = TEXT("뉴욕 스타일 조개 피자");
			dough = TEXT("씬 크러스트 도우");
			sauce = TEXT("마리나라 소스");

			toppings.push_back(TEXT("잘게 썬 레지아노 치즈"));
			toppings.push_back(TEXT("Long Island Sound산 신선한 조개"));
		}
	};
}