from pytest import *
from WeaterData import WeatherData
from Display import *

def test_watherdata(capsys):
    weatherdata = WeatherData()
    CurrentConditionsDisplay(weatherdata)
    StatisticsDisplay(weatherdata)
    ForecastDisplay(weatherdata)
    HeatIndexDisplay(weatherdata)
    weatherdata.setMeasurements(80, 65, 30.4)
    captured = capsys.readouterr()
    assert captured.out == "현재 상태: 온도 80.0F, 습도 65.0%\n" + "평균/최고/최저 온도 = 80.0/80.0/80.0\n" + "기상 예보: 날씨가 좋아지고 있습니다!\n" + "체감 온도: 82.95535\n"
    weatherdata.setMeasurements(82, 70, 29.2)
    captured = capsys.readouterr()
    assert captured.out == "현재 상태: 온도 82.0F, 습도 70.0%\n" + "평균/최고/최저 온도 = 81.0/82.0/80.0\n" + "기상 예보: 쌀쌀하며 비가 올 것 같습니다.\n" + "체감 온도: 86.90123\n"
    weatherdata.setMeasurements(78, 90, 29.2)
    captured = capsys.readouterr()
    assert captured.out == "현재 상태: 온도 78.0F, 습도 90.0%\n" + "평균/최고/최저 온도 = 80.0/82.0/78.0\n" + "기상 예보: 지금과 비슷할 것 같습니다.\n" + "체감 온도: 83.64967\n"



