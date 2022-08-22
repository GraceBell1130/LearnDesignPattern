#pragma once
#include "stdafx.h"
#include "Observer.hpp"
class ISubject {
public:
	virtual void regsisterObserver(std::unique_ptr<IObserver> o) = 0;
	virtual void removeObserver(std::unique_ptr<IObserver> o) = 0;
	virtual void notifyObservers() = 0;
};