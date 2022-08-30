#pragma once
#include "../stdafx.h"
#include "thick_crust_dough.hpp"
#include "marinara_sauce.hpp"
#include "reggiano_cheese.hpp"
#include "garlic.hpp"
#include "onion.hpp"
#include "mushroom.hpp"
#include "red_pepper.hpp"
#include "sliced_pepperoni.hpp"
#include "pizza_ingredient_factory_interface.hpp"
#include "fresh_clams.hpp"

namespace AbstractFactory {
	class NyPizzaIngredientFactory : public PizzaIngredientFactory {
	public:
		std::unique_ptr<Dough> createDough() override {
			return std::make_unique<ThickCrustDough>();
		}

		std::unique_ptr<Sauce> createSauce() override {
			return std::make_unique<MarinaraSauce>();
		}

		std::unique_ptr<Cheese> createCheese() override {
			return std::make_unique<ReggianoCheese>();
		}

		std::vector<std::unique_ptr<Veggies>> createVeggies() override {
			std::vector<std::unique_ptr<Veggies>> veggies;
			veggies.push_back(std::make_unique<Garlic>());
			veggies.push_back(std::make_unique<Onion>());
			veggies.push_back(std::make_unique<Mushroom>());
			veggies.push_back(std::make_unique<RedPepper>());

			return std::move(veggies);
		}

		std::unique_ptr<Pepperoni> createPepperoni() override {
			return std::make_unique<SlicedPepperoni>();
		}
		std::unique_ptr<Clams> createClam() override {
			return std::make_unique<FreshClams>();
		}
	};
}