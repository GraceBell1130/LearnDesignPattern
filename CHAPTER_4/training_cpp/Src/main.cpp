#include "stdafx.h"
#include "FactoryMethod/pizza.hpp"
#include "FactoryMethod/pizza_store.hpp"
#include "FactoryMethod/ny_style_pizza_store.hpp"
#include "FactoryMethod/chicago_style_pizza_store.hpp"

int main() {
	std::wcout.imbue(std::locale("korean"));
	std::unique_ptr<FactoryMethod::PizzaStore> nyStore = std::make_unique<FactoryMethod::NyStylePizzaStore>();
	std::unique_ptr<FactoryMethod::PizzaStore> chicahoStore = std::make_unique<FactoryMethod::ChicagoStylePizzaStore>();

	std::unique_ptr<FactoryMethod::Pizza> pizza = nyStore->orderPizza(TEXT("cheese"));
	std::wcout << TEXT("에단이 주문한") << pizza->getName() << std::endl << std::endl;
	std::wcout.flush();

	pizza = chicahoStore->orderPizza(TEXT("cheese"));
	std::wcout << TEXT("조엘이 주문한") << pizza->getName() << std::endl << std::endl;



}