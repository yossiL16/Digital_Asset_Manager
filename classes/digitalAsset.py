import datetime
from abc import ABC, abstractmethod
import datetime
import time

class DigitalAsset(ABC):
    def __init__(self, name:str, registration_date:datetime.date, cost:float):
        self.__name = name
        self.__registration_date = registration_date
        self.__cost = cost

    @property
    def name(self):
        return self.__name

    @property
    def registration_date(self):
        return self.__registration_date.isoformat()

    @property
    def cost(self):
        return self.__cost

    @abstractmethod
    def calculate_value(self) -> float:
        pass

    @abstractmethod
    def asset_type(self) -> str:
        pass
