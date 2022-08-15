#!/usr/bin/env python3

"""
    Theory: https://www.youtube.com/watch?v=_BpmfnqjgzQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=2
            https://www.dofactory.com/net/observer-design-pattern
            https://en.wikipedia.org/wiki/Observer_pattern
"""

from abc import ABC, abstractmethod
from typing import List


# interfaces
class IObserver(ABC):
    @abstractmethod
    def update():
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(observer: IObserver):
        pass

    @abstractmethod
    def notify():
        pass


# concrete implementations
class WeatherStation(IObservable):
    temp: int
    _observers: List[IObserver]
    def __init__(self, temp: int):
        self.temp = temp
        self._observers = list();
    
    def add_observer(self, observer: IObserver):
        self._observers.append(observer)
    
    def remove_observer(self, observer: IObserver):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update()
    
    def get_temp(self) -> int:
        return self.temp

    def set_temp(self, new_temp: int):
        self.temp = new_temp
        # self.notify()


class PhoneDisplay(IObserver):
    weather_station: WeatherStation
    def __init__(self, station: WeatherStation):
        self.weather_station = station
        # can skip the above variable by taking updated state as argument to update method
        # so no need to call weather_station for value

    def update(self):
        print(f"Phone: current temperature is {self.weather_station.get_temp()}°C")


# can obviously use strategy pattern or inheritance here
class CarDisplay(IObserver):
    weather_station: WeatherStation
    def __init__(self, station: WeatherStation):
        self.weather_station = station
        # can skip above variable just like PhoneDisplay

    def update(self):
        print(f"Car: current temperature is {self.weather_station.get_temp()}°C")


if __name__ == "__main__":
    # observable
    city_station = WeatherStation(25)

    # observers
    phone = PhoneDisplay(city_station)
    car = CarDisplay(city_station)

    # subscribe observers
    city_station.add_observer(phone)
    city_station.add_observer(car)

    # update temp
    city_station.set_temp(27)

    # notify all observers
    city_station.notify()  # we can actually skip this call by having it inside set_temp

    print()
    # testing remove_observer
    city_station.remove_observer(car)
    city_station.set_temp(26)
    city_station.notify()


    """ 
        output:
        Phone: current temperature is 27°C
        Car: current temperature is 27°C

        Phone: current temperature is 26°C
    """

