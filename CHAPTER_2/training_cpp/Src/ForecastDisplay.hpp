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
		std::cout << "��� ����: ";
		if (currentPressure > lastPressure) {
			std::cout << "������ �������� �ֽ��ϴ�." << std::endl;
		}
		else if (currentPressure == lastPressure) {
			std::cout << "���ݰ� ����� �� �����ϴ�." << std::endl;
		}
		else if (currentPressure < lastPressure) {
			std::cout << "�ҽ��ϸ� �� �� �� �����ϴ�." << std::endl;
		}
	}
};