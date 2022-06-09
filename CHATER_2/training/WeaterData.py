from typing import List
from Subject import ISubject
from Observer import IObserver

class WeatherData(ISubject):
    def __init__(self) -> None:
        super().__init__()
        self.observers :List[IObserver] = []
        self.temperature :float
        self.humidity :float
        self.pressure :float

    def registerObserver(self, o: IObserver):
        self.observers.append(o)

    def removeObserver(self, o: IObserver):
        self.observers.remove(o)
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature :float, humidity :float, pressure :float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()