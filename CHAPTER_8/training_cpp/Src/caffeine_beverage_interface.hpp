#pragma once
#include "stdafx.h"

class CaffeineBeverage {
public:
	void PrepareRecipe() {
		BoilWater();
		Brew();
		PourInCup();
		if (CustomerWantsCondiments()) {
			AddCondiments();
		}
	} 
	
	virtual void Brew() = 0;
	virtual void AddCondiments() = 0;

	void BoilWater() {
		std::tcout << TEXT("Boiling water") << std::endl;
	}

	void PourInCup() {
		std::tcout << TEXT("Pouring into cup") << std::endl;
	}

	virtual bool CustomerWantsCondiments() {
		return true;
	}
};