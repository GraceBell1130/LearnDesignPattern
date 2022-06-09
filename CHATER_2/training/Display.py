from typing import IO
from Observer import IObserver
from DisplayElement import IDisplayElement
from WeaterData import WeatherData

class CurrentConditionsDisplay(IObserver, IDisplayElement):
    def __init__(self, weatherData :WeatherData) -> None:
        self.temperature :float = 0
        self.humidity :float = 0
        self.weatherData :WeatherData = weatherData
        self.weatherData.registerObserver(self)
    
    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()
    ''' Oberser에서 데이터를 가져오는 Pull 방식
    def update(self):
        self.temperature = weatherData.getTemperature()
        self.humidity = weatherData.getHumidity()
        self.display()
    '''    
    def display(self):
        print(f"현재 상태: 온도 {self.temperature:.1f}F, 습도 {self.humidity:.1f}%")


class StatisticsDisplay(IObserver, IDisplayElement):
    def __init__(self, weatherData :WeatherData) -> None:
        self.maxTemp :float = 0
        self.minTemp :float = 200
        self.tempSum :float = 0
        self.numReadings :int = 0
        self.weatherData :WeatherData = weatherData
        self.weatherData.registerObserver(self)
    
    def update(self, temp: float, humidity: float, pressure: float):
        self.tempSum += temp
        self.numReadings+=1

        if temp > self.maxTemp:
            self.maxTemp = temp
        if temp < self.minTemp:
            self.minTemp = temp
        self.display()

    def display(self):
        print(f"평균/최고/최저 온도 = {self.tempSum/self.numReadings:.1f}/{self.maxTemp:.1f}/{self.minTemp:.1f}")

        
class ForecastDisplay(IObserver, IDisplayElement):
    def __init__(self, weatherData :WeatherData) -> None:
        self.currentPressure :float = 29.92;  
        self.lastPressure :float = 0
        self.weatherData :WeatherData = weatherData
        self.weatherData.registerObserver(self)
    
    def update(self, temp: float, humidity: float, pressure: float):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure
        self.display()

    def display(self):
        result = ""
        if self.currentPressure > self.lastPressure:
            result = "날씨가 좋아지고 있습니다!"
        elif self.currentPressure == self.lastPressure:
            result = "지금과 비슷할 것 같습니다."
        elif self.currentPressure < self.lastPressure:
            result = "쌀쌀하며 비가 올 것 같습니다."
        print(f"기상 예보: {result}")


class HeatIndexDisplay(IObserver, IDisplayElement):
    def __init__(self, weatherData :WeatherData) -> None:
        self.heatindex :float = 0
        self.weatherData :WeatherData = weatherData
        self.weatherData.registerObserver(self)
    
    def update(self, temp: float, humidity: float, pressure: float):
        self.heatindex = (float)((16.923 + (0.185212 * temp) + (5.37941 * humidity) - (0.100254 * temp * humidity) +
		(0.00941695 * (temp * temp)) + (0.00728898 * (humidity * humidity)) +
		(0.000345372 * (temp * temp * humidity)) - (0.000814971 * (temp * humidity * humidity)) +
		(0.0000102102 * (temp * temp * humidity * humidity)) - (0.000038646 * (temp * temp * temp)) + (0.0000291583 *  
		(humidity * humidity * humidity)) + (0.00000142721 * (temp * temp * temp * humidity)) +
		(0.000000197483 * (temp * humidity * humidity * humidity)) - (0.0000000218429 * (temp * temp * temp * humidity * humidity)) +     
		0.000000000843296 * (temp * temp * humidity * humidity * humidity)) -
		(0.0000000000481975 * (temp * temp * temp * humidity * humidity * humidity)));
        self.display()
        
    def display(self):
        print(f"체감 온도: {self.heatindex:.5f}")