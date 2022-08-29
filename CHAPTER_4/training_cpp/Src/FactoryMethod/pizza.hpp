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
			std::wcout << TEXT("�غ� ��: " + name) << std::endl;
			std::wcout << TEXT("���츦 ������ ��...") << std::endl;
			std::wcout << TEXT("�ҽ��� �Ѹ��� ��...") << std::endl;
			std::wcout << TEXT("������ �ø��� ��...") << std::endl;
			for (std::wstring topping : toppings) {
				std::wcout << TEXT(" " + topping) << std::endl;
			}
		}

		void bake() {
			std::wcout << TEXT("175������ 25�� �� ����") << std::endl;
		}

		virtual void cut() {
			std::wcout << TEXT("���ڸ� �缱���� �ڸ���") << std::endl;
		}

		void box() {
			std::wcout << TEXT("���ڿ� ���� ���") << std::endl;
		}

		std::wstring getName() {
			return name;
		}

	};
}
