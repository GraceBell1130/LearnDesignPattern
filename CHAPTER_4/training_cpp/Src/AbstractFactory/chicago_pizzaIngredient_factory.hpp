#pragma once
#include "../stdafx.h"
#include "thick_crust_dough.hpp"
#include "plum_tomato_sauce.hpp"
#include "mozzarella_cheese.hpp"
#include "black_olives.hpp"
#include "spinach.hpp"
#include "sliced_pepperoni.hpp"
#include "eggplant.hpp"
#include "pizza_ingredient_factory_interface.hpp"
#include "frozen_clams.hpp"

namespace AbstractFactory {
	class ChicagoPizzaIngredientFactory : public PizzaIngredientFactory {
	public:
		std::unique_ptr<Dough> createDough() override {
			return std::make_unique<ThickCrustDough>();
		}

		std::unique_ptr<Sauce> createSauce() override {
			return std::make_unique<PlumTomatoSauce>();
		}

		std::unique_ptr<Cheese> createCheese() override {
			return std::make_unique<MozzarellaCheese>();
		}

		std::vector<std::unique_ptr<Veggies>> createVeggies() override {
			std::vector<std::unique_ptr<Veggies>> veggies;
			veggies.push_back(std::make_unique<BlackOlives>());
			veggies.push_back(std::make_unique<Spinach>());
			veggies.push_back(std::make_unique<Eggplant>());

			return std::move(veggies);
		}

		std::unique_ptr<Pepperoni> createPepperoni() override {
			return std::make_unique<SlicedPepperoni>();
		}
		std::unique_ptr<Clams> createClam() override {
			return std::make_unique<FrozenClams>();
		}
	};
}