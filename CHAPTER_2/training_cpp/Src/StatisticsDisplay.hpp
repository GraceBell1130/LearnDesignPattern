#pragma once
#include "stdafx.h"
#include "Observer.hpp"
#include "DisplayElement.hpp"
#include "WeatherData.hpp"

class StatisticsDisplay : public IObserver, IDisplayElement {
private:
	float maxTemp = 0.0f;
	float minTemp = 200;
	float tempSum = 0.0f;
	int numReadings = 0;

public:
	StatisticsDisplay() = default;

	void update(float temp, float humidity, float pressure) {
		tempSum += temp;
		numReadings++;

		if (temp > maxTemp) {
			maxTemp = temp;
		}

		if (temp < minTemp) {
			minTemp = temp;
		}
		display();
	}

	void display() {
		std::cout << "평균/최고/최저 온도 = " << (tempSum / numReadings) << "/" << maxTemp << "/" << minTemp << std::endl;
	}
};