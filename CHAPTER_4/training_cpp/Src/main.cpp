#include "stdafx.h"

#include "FactoryMethod/pizza.hpp"
#include "FactoryMethod/pizza_store.hpp"
#include "FactoryMethod/ny_style_pizza_store.hpp"
#include "FactoryMethod/chicago_style_pizza_store.hpp"

#include "AbstractFactory/pizza.hpp"
#include "AbstractFactory/pizza_store.hpp"
#include "AbstractFactory/ny_pizza_store.hpp"
#include "AbstractFactory/chicago_pizza_store.hpp"

int main() {
	std::wcout.imbue(std::locale("korean"));
	{
		std::unique_ptr<FactoryMethod::PizzaStore> ny_store = std::make_unique<FactoryMethod::NyStylePizzaStore>();
		std::unique_ptr<FactoryMethod::PizzaStore> chicaho_store = std::make_unique<FactoryMethod::ChicagoStylePizzaStore>();

		std::unique_ptr<FactoryMethod::Pizza> pizza = ny_store->orderPizza(TEXT("cheese"));
		std::wcout << TEXT("에단이 주문한 : ") << pizza->getName() << std::endl << std::endl;

		pizza = chicaho_store->orderPizza(TEXT("cheese"));
		std::wcout << TEXT("조엘이 주문한 : ") << pizza->getName() << std::endl << std::endl;
	}
	{
		std::unique_ptr<AbstractFactory::PizzaStore> ny_store = std::make_unique<AbstractFactory::NyStylePizzaStore>();
		std::unique_ptr<AbstractFactory::PizzaStore> chicaho_store = std::make_unique<AbstractFactory::ChicagoStylePizzaStore>();
		
		std::unique_ptr<AbstractFactory::Pizza> pizza = ny_store->orderPizza(TEXT("cheese"));
		std::wcout << TEXT("에단이 주문한 : ") << pizza->getName() << std::endl << std::endl;

		pizza = chicaho_store->orderPizza(TEXT("cheese"));
		std::wcout << TEXT("조엘이 주문한 : ") << pizza->getName() << std::endl << std::endl;
	}



}