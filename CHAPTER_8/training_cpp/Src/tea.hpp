#pragma once
#include "stdafx.h"
#include "caffeine_beverage_interface.hpp"

class Tea : public CaffeineBeverage {
public:
	void Brew() override {
		std::tcout << TEXT("Steeping the tea") << std::endl;
	}

	void AddCondiments() override {
		std::tcout << TEXT("Adding Lemon") << std::endl;
	}

	bool CustomerWantsCondiments() override {
		if (GetUserInput() == 'y') {
			return true;
		}
		else {
			return false;
		}
	}
private:
	char GetUserInput() {
		char answer = 'y';
		std::tcout << TEXT("Would you like milk and sugar with your coffee (y/n)? ") << std::endl;
		std::cin >> answer;
		return answer;
	}
};