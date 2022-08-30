#pragma once
#include "../stdafx.h"
#include "pizza.hpp"
#include "pizza_store.hpp"
#include "chicago_pizzaIngredient_factory.hpp"
#include "cheese_pizza.hpp"
#include "veggie_pizza.hpp"
#include "clam_pizza.hpp"
#include "pepperoni_pizza.hpp"

namespace AbstractFactory {
	class ChicagoStylePizzaStore : public PizzaStore {
	public:
		std::unique_ptr<Pizza> createPizza(std::wstring type) override {
			std::unique_ptr<Pizza> pizza = nullptr;
			std::unique_ptr<PizzaIngredientFactory> ingredient_factory = std::make_unique<ChicagoPizzaIngredientFactory>();
			
			if (type == TEXT("cheese")) {
				pizza = std::make_unique<CheesePizza>(std::move(ingredient_factory));
				pizza->setName(TEXT("Chicago Style Cheese Pizza"));
			}
			else if (type == TEXT("veggie")) {
				pizza = std::make_unique<VeggiePizza>(std::move(ingredient_factory));
			}
			else if (type == TEXT("clam")) {
				pizza = std::make_unique<ClamPizza>(std::move(ingredient_factory));
			}
			else if (type == TEXT("pepperoni")) {
				pizza = std::make_unique<PepperoniPizza>(std::move(ingredient_factory));
			}

			return std::move(pizza);
		}
	};
}