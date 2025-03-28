from exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        if not isinstance(value, bool):
            raise ValueError("Состояние двигателя должно быть True или False")
        self._started = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Вес транспортного средства должен быть положительным.")
        self._weight = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Количество топлива не может быть отрицательным.")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value <= 0:
            raise ValueError("Расход топлива должен быть положительным.")
        self._fuel_consumption = value

    def start(self):
        if self.started:
            raise ValueError("Двигатель уже запущен.")
        if self.fuel <= 0:
            raise LowFuelError("Недостаточно топлива для запуска двигателя.")
        self.started = True

    def move(self, distance):
        if not self.started:
            raise ValueError("Двигатель не запущен.")
        required_fuel = self.fuel_consumption * (distance / 100)
        if required_fuel > self.fuel:
            raise NotEnoughFuel("Топлива недостаточно для преодоления этого расстояния.")
        self.fuel -= required_fuel
