#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class ChicahoStyleVeggiePizza : public Pizza {
	public:
		ChicahoStyleVeggiePizza() {
			name = TEXT("��ī�� ��Ÿ�� �� �� ��ä ����");
			dough = TEXT("���� �β��� ũ����Ʈ ����");
			sauce = TEXT("�÷��丶�� �ҽ�");

			toppings.push_back(TEXT("�߰� ������ ��¥���� ġ��"));
			toppings.push_back(TEXT("���� �ø���"));
			toppings.push_back(TEXT("�ñ�ġ"));
			toppings.push_back(TEXT("����"));
		}

		void cut() override {
			std::wcout << TEXT("�׸� ������� ���� �ڸ���") << std::endl;
		}
	};
}