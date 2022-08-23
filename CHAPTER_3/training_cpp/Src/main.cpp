#include "stdafx.h"
#include "beverage.hpp"
#include "espresso.hpp"
#include "dark_roast.hpp"
#include "houseblend.hpp"
#include "Moca.hpp"
#include "Whip.hpp"
#include "Soy.hpp"

int main() {
	std::wcout.imbue(std::locale("korean"));
	std::shared_ptr<Beverage> beverage = std::make_shared<Espresso>();
	//std::wcout << beverage->getDescription() << TEXT(" $") << beverage->cost() << std::endl;

	std::shared_ptr<Beverage> beverage2 = std::make_shared<DarkRoast>();
	beverage2 = std::make_shared<Moca>(beverage2);
	beverage2 = std::make_shared<Moca>(beverage2);
	beverage2 = std::make_shared<Whip>(beverage2);
	std::wcout << beverage2->getDescription() << TEXT(" $") << beverage2->cost() << std::endl;

	std::shared_ptr<Beverage> beverage3 = std::make_shared<HouseBlend>();
	beverage3 = std::make_shared<Soy>(beverage3);
	beverage3 = std::make_shared<Moca>(beverage3);
	beverage3 = std::make_shared<Whip>(beverage3);
	//std::wcout << beverage3->getDescription() << TEXT(" $") << beverage3->cost() << std::endl;
}