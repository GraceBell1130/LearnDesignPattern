#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class ChicahoStyleCheesePizza : public Pizza {
	public:
		ChicahoStyleCheesePizza() {
			name = TEXT("��ī�� ��Ÿ�� �� �� ġ�� ����");
			dough = TEXT("���� �β��� ũ����Ʈ ����");
			sauce = TEXT("�÷��丶�� �ҽ�");

			toppings.push_back(TEXT("�߰� ������ ��¥���� ġ��"));
		}

		void cut() override {
			std::wcout << TEXT("�׸� ������� ���� �ڸ���") << std::endl;
		}
	};
}