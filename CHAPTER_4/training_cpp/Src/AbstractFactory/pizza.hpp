#pragma once
#include "../stdafx.h"
#include "dough_interface.hpp"
#include "sauce_interface.hpp"
#include "veggies_interface.hpp"
#include "cheese_interface.hpp"
#include "pepperoni_interface.hpp"
#include "clams_interface.hpp"

namespace AbstractFactory {
	class Pizza {
	protected:
		std::wstring name = TEXT("");
		std::unique_ptr<Dough> dough = nullptr;
		std::unique_ptr<Sauce> sauce = nullptr;
		std::vector<std::unique_ptr<Veggies>> veggies;
		std::unique_ptr<Cheese> cheese = nullptr;
		std::unique_ptr<Pepperoni> pepperoni = nullptr;
		std::unique_ptr<Clams> clam = nullptr;

	public:
		virtual void prepare() = 0;

		void bake() {
			std::wcout << TEXT("Bake for 25 minutes at 350") << std::endl;
		}

		void cut() {
			std::wcout << TEXT("Cutting the pizza into diagonal slices") << std::endl;
		}

		void box() {
			std::wcout << TEXT("Place pizza in official PizzaStore box") << std::endl;
		}

		void setName(std::wstring name) {
			this->name = name;
		}
		
		std::wstring getName() {
			return name;
		}

		std::wstring toString() {
			std::wstring result = TEXT("---- ") + name + TEXT(" ----\n");
			if (nullptr != dough) {
				result.append(dough->tostring() + TEXT("\n"));
			}
			if (nullptr != sauce) {
				result.append(sauce->tostring() + TEXT("\n"));
			}
			if (nullptr != cheese) {
				result.append(cheese->tostring() + TEXT("\n"));
			}
			if (false == veggies.empty()) {
				for (int index = 0; index < veggies.size() - 1; index++) {
					result.append(veggies.at(index)->tostring() + TEXT(", \n"));
				}
				result.append(veggies.at(veggies.size() - 1)->tostring() + TEXT("\n"));
			}
			if (nullptr != clam) {
				result.append(clam->tostring() + TEXT("\n"));
			}
			if (nullptr != pepperoni) {
				result.append(pepperoni->tostring() + TEXT("\n"));
			}
		}
	};
}
