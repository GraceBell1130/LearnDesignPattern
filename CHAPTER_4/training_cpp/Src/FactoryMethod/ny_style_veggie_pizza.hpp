#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleVeggiePizza : public Pizza {
	public:
		NyStyleVeggiePizza() {
			name = TEXT("���� ��Ÿ�� ��ä ����");
			dough = TEXT("�� ũ����Ʈ ����");
			sauce = TEXT("�������� �ҽ�");

			toppings.push_back(TEXT("�߰� �� �����Ƴ� ġ��"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
			toppings.push_back(TEXT("����"));
		}
	};
}