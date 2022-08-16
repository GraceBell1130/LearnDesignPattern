#include "stdafx.h"
#include "MallardDuck.hpp"
#include "ModelDuck.hpp"
#include "FlyRocketPowered.hpp"
int main() 
{
	std::wcout.imbue(std::locale("korean"));
	std::unique_ptr<Duck> mallard = std::make_unique<MallardDuck>();
	mallard->performQuack();
	mallard->performFly();

	std::unique_ptr<Duck> model = std::make_unique<ModelDuck>();
	model->performFly();
	model->setFlyBehavior(std::make_unique<FlyRocketPowered>());
	model->performFly();
}