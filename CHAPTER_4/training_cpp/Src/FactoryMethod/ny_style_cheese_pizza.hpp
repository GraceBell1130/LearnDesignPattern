#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleCheesePizza : public Pizza {
	public:
		NyStyleCheesePizza() {
			name = TEXT("���� ��Ÿ�� �ҽ��� ġ�� ����");
			dough = TEXT("�� ũ����Ʈ ����");
			sauce = TEXT("�������� �ҽ�");

			toppings.push_back(TEXT("�߰� �� �����Ƴ� ġ��"));
		}
	};
}