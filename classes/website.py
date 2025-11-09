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


