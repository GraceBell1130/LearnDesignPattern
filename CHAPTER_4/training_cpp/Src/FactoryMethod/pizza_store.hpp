#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace FactoryMethod {
	class PizzaStore {
	protected:
		virtual std::unique_ptr<Pizza> createPizza(std::wstring type) = 0;
	public:
		std::unique_ptr<Pizza> orderPizza(std::wstring type) {
			std::unique_ptr<Pizza> pizza;

			pizza = createPizza(type);

			pizza->prepare();
			pizza->bake();
			pizza->cut();
			pizza->box();

			return std::move(pizza);
		}
	};
}
