#pragma once
#include "../stdafx.h"
#include "pizza.hpp"
#include "pizza_store.hpp"
#include "chicago_style_cheese_pizza.hpp"
#include "chicago_style_pepperoni_pizza.hpp"
#include "chicago_style_clam_pizza.hpp"
#include "chicago_style_veggie_pizza.hpp"

namespace FactoryMethod {
	class ChicagoStylePizzaStore : public PizzaStore {
	public:
		std::unique_ptr<Pizza> createPizza(std::wstring type) override {
			std::unique_ptr<Pizza> pizza;

			if (type == TEXT("cheese")) {
				pizza = std::make_unique<ChicahoStyleCheesePizza>();
			}
			else if (type == TEXT("pepperoni")) {
				pizza = std::make_unique<ChicahoStylePepperoniPizza>();
			}
			else if (type == TEXT("clam")) {
				pizza = std::make_unique<ChicahoStyleClamPizza>();
			}
			else if (type == TEXT("veggie")) {
				pizza = std::make_unique<ChicahoStyleVeggiePizza>();
			}

			return std::move(pizza);
		}
	};
}