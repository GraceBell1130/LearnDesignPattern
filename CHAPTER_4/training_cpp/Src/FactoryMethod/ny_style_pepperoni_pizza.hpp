#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStylePepperoniPizza : public Pizza {
	public:
		NyStylePepperoniPizza() {
			name = TEXT("���� ��Ÿ�� ����δ� ����");
			dough = TEXT("�� ũ����Ʈ ����");
			sauce = TEXT("�������� �ҽ�");

			toppings.push_back(TEXT("�߰� �� �����Ƴ� ġ��"));
			toppings.push_back(TEXT("��� �� ����δ�"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
		}
	};
}