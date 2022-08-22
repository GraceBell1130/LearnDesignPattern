#pragma once
#include "stdafx.h"
#include "Observer.hpp"
#include "DisplayElement.hpp"
#include "WeatherData.hpp"

class ForecastDisplay : public IObserver, IDisplayElement {
private:
	float currentPressure = 29.92f;
	float lastPressure = 0;

public:
	ForecastDisplay() = default;

	void update(float temp, float humidity, float pressure) {
		lastPressure = currentPressure;
		currentPressure = pressure;
		display();
	}

	void display() {
		std::cout << "기상 예보: ";
		if (currentPressure > lastPressure) {
			std::cout << "날씨가 좋아지고 있습니다." << std::endl;
		}
		else if (currentPressure == lastPressure) {
			std::cout << "지금과 비슷할 것 같습니다." << std::endl;
		}
		else if (currentPressure < lastPressure) {
			std::cout << "쌀쌀하며 비가 올 것 같습니다." << std::endl;
		}
	}
};