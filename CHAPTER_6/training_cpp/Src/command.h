#pragma once
#include "stdafx.h"

class Command {
public:
	virtual void Execute() = 0;
	virtual std::tstring Name() = 0;
};