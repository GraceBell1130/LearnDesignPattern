#pragma once
#include "../stdafx.h"
#include "dough_interface.hpp"
#include "sauce_interface.hpp"
#include "cheese_interface.hpp"
#include "veggies_interface.hpp"
#include "pepperoni_interface.hpp"
#include "clams_interface.hpp"

namespace AbstractFactory {
	class PizzaIngredientFactory {
	public:
		virtual std::unique_ptr<Dough> createDough() = 0;
		virtual std::unique_ptr<Sauce> createSauce() = 0;
		virtual std::unique_ptr<Cheese> createCheese() = 0;
		virtual std::vector<std::unique_ptr<Veggies>> createVeggies() = 0;
		virtual std::unique_ptr<Pepperoni> createPepperoni() = 0;
		virtual std::unique_ptr<Clams> createClam() = 0;
	};
}