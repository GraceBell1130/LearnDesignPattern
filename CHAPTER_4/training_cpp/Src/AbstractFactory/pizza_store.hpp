#pragma once
#include "../stdafx.h"
#include "pizza.hpp"

namespace AbstractFactory {
	class PizzaStore {
	protected:
		virtual std::unique_ptr<Pizza> createPizza(std::wstring type) = 0;
	public:
		std::unique_ptr<Pizza> orderPizza(std::wstring type) {
			std::unique_ptr<Pizza> pizza = createPizza(type);
			std::wcout << TEXT("--- making a ") << pizza->getName() << TEXT(" ---") << std::endl;

			pizza->prepare();
			pizza->bake();
			pizza->cut();
			pizza->box();

			return std::move(pizza);
		}
	};
}
