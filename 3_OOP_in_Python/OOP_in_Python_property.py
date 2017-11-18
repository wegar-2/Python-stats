# ----- This lesson is simply a walk through the tutorial: https://www.programiz.com/python-programming/property


class CelsiusTemperature(object):

    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature

    def get_temperature_in_fahrenheit(self):
        return self.celsius_temperature*1.8 + 32


ct1 = CelsiusTemperature(celsius_temperature=12)
print(ct1.get_temperature_in_fahrenheit())
print(ct1.__dict__)


# ----- New version of the CelsiusTemperature class that uses getters and setters