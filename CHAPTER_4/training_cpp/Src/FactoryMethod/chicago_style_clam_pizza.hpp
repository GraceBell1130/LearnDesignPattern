#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class ChicahoStyleClamPizza : public Pizza {
	public:
		ChicahoStyleClamPizza() {
			name = TEXT("��ī�� ��Ÿ�� �� �� ���� ����");
			dough = TEXT("���� �β��� ũ����Ʈ ����");
			sauce = TEXT("�÷��丶�� �ҽ�");

			toppings.push_back(TEXT("�߰� ������ ��¥���� ġ��"));
			toppings.push_back(TEXT("Chesapeake Bay�� �õ� ����"));
		}

		void cut() override {
			std::wcout << TEXT("�׸� ������� ���� �ڸ���") << std::endl;
		}
	};
}