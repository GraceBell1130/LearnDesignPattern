#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class NyStyleClamPizza : public Pizza {
	public:
		NyStyleClamPizza() {
			name = TEXT("���� ��Ÿ�� ���� ����");
			dough = TEXT("�� ũ����Ʈ ����");
			sauce = TEXT("�������� �ҽ�");

			toppings.push_back(TEXT("�߰� �� �����Ƴ� ġ��"));
			toppings.push_back(TEXT("Long Island Sound�� �ż��� ����"));
		}
	};
}