from typing import assert_type

from classes.reportable import Reportable
from classes.digitalAsset import DigitalAsset
import datetime

class Website(DigitalAsset, Reportable):
    def __init__(self, name: str, registration_date: datetime.date, cost: float, monthly_traffic:int,monetization_rate:float):
        super().__init__(name, registration_date, cost)
        self.__monthly_traffic = monthly_traffic
        self.__monetization_rate = monetization_rate

    def asset_type(self):
        return "WEBSITE"

    def calculate_value(self):
        value = self.__monthly_traffic * self.__monetization_rate * 12
        return value

    def to_report_line(self):
        return f"type : {self.asset_type()}, name : {self.name}, date : {self.registration_date}, cost : {self.cost}, monthly traffic : {self.__monthly_traffic}, monetization rate : {self.__monetization_rate}, Current value : {self.calculate_value()} "
