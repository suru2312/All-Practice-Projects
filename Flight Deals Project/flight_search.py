import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_flight_price(self, origin, destination):
        SERP_ENDPOINT = os.getenv("SERP_ENDPOINT")
        
        parameters = {
            "engine": "google_flights",
            "departure_id": origin,
            "arrival_id": destination,
            "outbound_date": "2026-05-01",
            "type": 2,
            "currency": "INR",
            "hl": "en",
            "api_key": SERP_API_KEY
        }
        
        response = requests.get(SERP_ENDPOINT, params = parameters)
        data = response.json()
        
        try:
            flights = data["best_flights"]
            cheapest_price = min(flight["price"] for flight in flights)
            return cheapest_price
        
        except KeyError:
            print("No flights found")
            return None