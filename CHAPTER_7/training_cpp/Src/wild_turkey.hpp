#pragma once
#include "stdafx.h"
#include "turkey_interface.hpp"

class WildTurkey : public Turkey {
	void gobble() {
		std::tcout << TEXT("���") << std::endl;
	}

	void fly() {
		std::tcout << TEXT("ª�� �Ÿ��� ���� �־��!") << std::endl;
	}
};