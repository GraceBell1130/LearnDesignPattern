#pragma once
#include "stdafx.h"
#include "turkey_interface.hpp"

class WildTurkey : public Turkey {
	void gobble() {
		std::tcout << TEXT("°ñ°ñ") << std::endl;
	}

	void fly() {
		std::tcout << TEXT("ÂªÀº °Å¸®¸¦ ³¯°í ÀÖ¾î¿ä!") << std::endl;
	}
};