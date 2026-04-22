import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data(self):
        response = requests.get(SHEET_ENDPOINT)
        data = response.json()
        return data["sheet1"]