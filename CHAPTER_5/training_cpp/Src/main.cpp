#include "stdafx.h"
#include "chocolate_boiler.hpp"

int main() {
	
	std::shared_ptr<ChocolateBoiler> instance1 = ChocolateBoiler::GetInstance();
	std::shared_ptr<ChocolateBoiler> instance2 = ChocolateBoiler::GetInstance();
	std::cout << instance1.get() << std::endl;
	std::cout << instance2.get() << std::endl;
	
}