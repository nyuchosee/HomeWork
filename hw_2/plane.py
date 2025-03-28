from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.cargo = cargo
        self.max_cargo = max_cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, amount):
        self._max_cargo = amount


    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("Перегрузка, груз превышает максимально допустимый.")
        self.cargo += amount

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before

