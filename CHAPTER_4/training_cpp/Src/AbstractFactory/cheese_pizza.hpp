#pragma once
#include "../stdafx.h"
#include "pizza.hpp"
#include "pizza_ingredient_factory_interface.hpp"

namespace AbstractFactory {
	class CheesePizza : public Pizza {
	private:
		std::unique_ptr<PizzaIngredientFactory> ingredient_factory;

	public:
		CheesePizza(std::unique_ptr<PizzaIngredientFactory> ingredient_factory) {
			this->ingredient_factory = std::move(ingredient_factory);
		}

		void prepare() override {
			std::wcout << TEXT("Preparing ") << this->name << std::endl;
			dough = ingredient_factory->createDough();
			sauce = ingredient_factory->createSauce();
			cheese = ingredient_factory->createCheese();
		}
	};
}