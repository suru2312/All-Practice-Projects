#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


data = data_manager.get_data()

for city in data:
    flight_price = flight_search.get_flight_price("IDR", city["iata"])
    
    if flight_price is not None and flight_price < city["price"]:
        message = (
            f"Low Price Alert! ✈️\n"
            f"IDR → {city['iata']}\n"
            f"City: {city['city']}\n"
            f"Price: ₹{flight_price}"
        )
        notification_manager.send_sms(message)