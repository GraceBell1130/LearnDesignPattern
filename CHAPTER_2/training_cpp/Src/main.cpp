#include "stdafx.h"
#include "WeatherData.hpp"
#include "CurrentConditionsDisplay.hpp"
#include "StatisticsDisplay.hpp"
#include "ForecastDisplay.hpp"
#include "HeatIndexDisplay.hpp"

int main() {
	std::unique_ptr<WeatherData> weatherdata = std::make_unique<WeatherData>();
	weatherdata->regsisterObserver(std::make_unique<CurrentConditionsDisplay>());
	weatherdata->regsisterObserver(std::make_unique<StatisticsDisplay>());
	weatherdata->regsisterObserver(std::make_unique<ForecastDisplay>());
	weatherdata->regsisterObserver(std::make_unique<HeatIndexDisplay>());
	
	weatherdata->setMeasurements(80, 65, 30.4f);
	weatherdata->setMeasurements(82, 70, 29.2f);
	weatherdata->setMeasurements(78, 90, 29.2f);
}