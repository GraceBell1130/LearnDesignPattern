#pragma once
#include "stdafx.h"
#include "Observer.hpp"
#include "Subject.hpp"

class WeatherData : public ISubject {
private:
	std::unique_ptr<std::list<std::unique_ptr<IObserver>>> observers = nullptr;
	float temperature = 0;
	float humidity = 0;
	float pressure = 0;

public:
	WeatherData() {
		observers = std::make_unique<std::list<std::unique_ptr<IObserver>>>();
	}

	void regsisterObserver(std::unique_ptr<IObserver> o) {
		observers->push_back(std::move(o));
	}

	void removeObserver(std::unique_ptr<IObserver> o) {
		observers->remove(std::move(o));
	}

	void notifyObservers() {
		for (std::list< std::unique_ptr<IObserver>>::iterator observer = observers->begin(); observer != observers->end(); observer++) {
			(*observer)->update(temperature, humidity, pressure);
		}
	}

	void measurementsChanged() {
		notifyObservers();
	}

	void setMeasurements(float temperature, float humidity, float pressure) {
		this->temperature = temperature;
		this->humidity = humidity;
		this->pressure = pressure;
		measurementsChanged();
	}
};