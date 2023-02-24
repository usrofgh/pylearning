# access to protected attributes always is via getters/setters

class Temperature:
    # probably you need to use attributes with _, cause without it you'll be get an error when realize properties
    def __init__(self, temperature: int, weather: str) -> None:
        self._temperature = temperature  # under the hood it'll call set_temperature if we specified
        # temperature = property(get_temperature, set_temperature)
        self._weather = weather  # with error - self.weather = weather. Any access to temp must go via property

    def get_temperature(self) -> int:
        return self._temperature

    def set_temperature(self, temperature: int) -> None:
        if -30 < temperature < 40:
            self._temperature = temperature
        else:
            raise ValueError(
                f"Invalid temperature value should be in the range of -30 and 40, but the actual is {temperature}")

    # expect of it you can use decorators, It'll be an attribue which you'll be able to get outside.
    # With help it you can get and set values
    temperature = property(get_temperature, set_temperature)  # creates erlier than init.  short version of below

    # temperature = property()
    # temperature = temperature.getter(get_temperature)
    # temperature = temperature.setter(set_temperature)
    # now we don't use set_ but use different decorators

    # weather = property(weather)
    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, weather: str):
        if weather != "kek":
            self._weather = weather
        else:
            raise ValueError(f"kek doesn't support")

    @property
    def info(self):
        return "its info about temp"


tt = Temperature(27, "Rainy")
print(tt.get_temperature())  # 27 // work after adding properties
tt.set_temperature(2)  # # 2 // work after adding properties
print(tt.temperature)  # property
# tt.temperature = 40  # error
tt.temperature = 0
print(tt.temperature)  # 0 // property

print(tt.weather)  # Rainy
tt.weather = "Sun"
print(tt.weather)  # Sun

# tt.weather = "kek"  # error
tt = Temperature(27, "kek")
print(tt.weather)  # kek - we don't have an error here. Because in init we don't use setter. For it you need to
# change self._weather to self.weather

print(tt.info)  # its info about temp
# tt.info = 1  # AttributeError: can't set attribute 'info' // cause we didn't specify setter - read-only attribute
