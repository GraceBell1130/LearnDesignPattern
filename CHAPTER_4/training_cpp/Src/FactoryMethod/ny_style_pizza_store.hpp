#pragma once
#include "../stdafx.h"
#include "pizza.hpp"
#include "pizza_store.hpp"
#include "ny_style_cheese_pizza.hpp"
#include "ny_style_pepperoni_pizza.hpp"
#include "ny_style_clam_pizza.hpp"
#include "ny_style_veggie_pizza.hpp"

namespace FactoryMethod {
	class NyStylePizzaStore : public PizzaStore {
	public:
		std::unique_ptr<Pizza> createPizza(std::wstring type) override {
			std::unique_ptr<Pizza> pizza;

			if (type == TEXT("cheese")) {
				pizza = std::make_unique<NyStyleCheesePizza>();
			}
			else if (type == TEXT("pepperoni")) {
				pizza = std::make_unique<NyStylePepperoniPizza>();
			}
			else if (type == TEXT("clam")) {
				pizza = std::make_unique<NyStyleClamPizza>();
			}
			else if (type == TEXT("veggie")) {
				pizza = std::make_unique<NyStyleVeggiePizza>();
			}

			return std::move(pizza);
		}
	};
}