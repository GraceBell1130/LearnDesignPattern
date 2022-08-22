#pragma once
#include "stdafx.h"
#include "Observer.hpp"
#include "DisplayElement.hpp"
#include "WeatherData.hpp"

class CurrentConditionsDisplay : public IObserver, IDisplayElement {
private:
	float temperature = 0; 
	float humidity = 0;

public:
	CurrentConditionsDisplay() = default;

	void update(float temp, float humidity, float pressure) {
		this->temperature = temp;
		this->humidity = humidity;
		display();
	}

	void display() {
		std::cout << "���� ����: �µ� " << temperature << "F, ���� " << humidity << "%" << std::endl;
	}
};