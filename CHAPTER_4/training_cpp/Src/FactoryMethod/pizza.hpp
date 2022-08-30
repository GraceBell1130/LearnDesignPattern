#pragma once
#include "../stdafx.h"

namespace FactoryMethod {
	class Pizza {
	protected:
		std::wstring name;
		std::wstring dough;
		std::wstring sauce;
		std::vector<std::wstring> toppings;
	public:
		void prepare() {
			std::wcout << TEXT("준비 중: " + name) << std::endl;
			std::wcout << TEXT("도우를 돌리는 중...") << std::endl;
			std::wcout << TEXT("소스를 뿌리는 중...") << std::endl;
			std::wcout << TEXT("토핑을 올리는 중...") << std::endl;
			for (std::wstring topping : toppings) {
				std::wcout << TEXT(" " + topping) << std::endl;
			}
		}

		void bake() {
			std::wcout << TEXT("175도에서 25분 간 굽기") << std::endl;
		}

		virtual void cut() {
			std::wcout << TEXT("피자를 사선으로 자르기") << std::endl;
		}

		void box() {
			std::wcout << TEXT("상자에 피자 담기") << std::endl;
		}

		std::wstring getName() {
			return name;
		}

	};
}
