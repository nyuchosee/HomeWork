from base import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, started=False, engine=None):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.engine = engine

    @property
    def engine(self):
        """Возвращаем двигатель автомобиля."""
        return self._engine

    @engine.setter
    def engine(self, value):
        """Устанавливаем двигатель автомобиля."""
        if not isinstance(value, Engine):
            raise ValueError("Должен быть передан объект класса Engine.")
        self._engine = value

    def set_engine(self, engine: Engine):
        self.engine = engine

