#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class ChicahoStyleClamPizza : public Pizza {
	public:
		ChicahoStyleClamPizza() {
			name = TEXT("시카고 스타일 딥 디쉬 조개 피자");
			dough = TEXT("아주 두꺼운 크러스트 도우");
			sauce = TEXT("플럼토마토 소스");

			toppings.push_back(TEXT("잘게 조각낸 모짜렐라 치즈"));
			toppings.push_back(TEXT("Chesapeake Bay산 냉동 조개"));
		}

		void cut() override {
			std::wcout << TEXT("네모난 모양으로 피자 자르기") << std::endl;
		}
	};
}