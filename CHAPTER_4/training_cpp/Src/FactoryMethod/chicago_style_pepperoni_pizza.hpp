#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class ChicahoStylePepperoniPizza : public Pizza {
	public:
		ChicahoStylePepperoniPizza() {
			name = TEXT("��ī�� ��Ÿ�� �� �� ����δ� ����");
			dough = TEXT("���� �β��� ũ����Ʈ ����");
			sauce = TEXT("�÷��丶�� �ҽ�");

			toppings.push_back(TEXT("�߰� ������ ��¥���� ġ��"));
			toppings.push_back(TEXT("���� �ø���"));
			toppings.push_back(TEXT("�ñ�ġ"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("��� �� ����δ�"));
		}

		void cut() override {
			std::wcout << TEXT("�׸� ������� ���� �ڸ���") << std::endl;
		}
	};
}