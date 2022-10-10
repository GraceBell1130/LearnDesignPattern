#include "stdafx.h"
#include "caffeine_beverage_interface.hpp"
#include "tea.hpp"
#include "coffee.hpp"

int main() {
	std::unique_ptr<Tea> tea = std::make_unique<Tea>();
	std::unique_ptr<Coffee> coffee = std::make_unique<Coffee>();

	std::tcout << TEXT("Making tea...") << std::endl;
	tea->PrepareRecipe();
	std::tcout << TEXT("Complete making tea") << std::endl << std::endl;

	std::tcout << TEXT("Making coffee...") << std::endl;
	coffee->PrepareRecipe();
	std::tcout << TEXT("Complete making coffee") << std::endl;

}