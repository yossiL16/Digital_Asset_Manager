from classes.digitalAsset import DigitalAsset
from classes.reportable import Reportable
import datetime

class MobileApp(DigitalAsset, Reportable):
    def __init__(self, name:str, registration_date:datetime.date, cost:float, downloads:int,avg_rating:float):
        super().__init__(name, registration_date, cost)
        self.__downloads = downloads
        self.__avg_rating = avg_rating

    def asset_type(self):
        return "MOBILE_APP"

    def calculate_value(self):
        value = self.__downloads * 0.5 + self.__avg_rating * 1000
        return value

    def to_report_line(self):
        return f"type : {self.asset_type()}, name : {self.name}, date : {self.registration_date}, cost : {self.cost}, downloads : {self.__downloads}, avg rating : {self.__avg_rating}, Current value : {self.calculate_value()}"