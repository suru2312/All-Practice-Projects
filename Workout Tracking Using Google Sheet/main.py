import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Your Personal data
GENDER = "male"
WEIGHT_KG = 87
HEIGHT_CM = 176
AGE = 24

# Nutrition APP Id and API Key
APP_ID = "app_623fa4787cd146a18f4c9619"
API_KEY = "nix_live_OsAL34vf1JJWrxQuqWtK5eLkgW11L7pN"

EXCERCISE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercise you did? : ")

# Nutrition API Call
headers = {
    "x-app-id" : "app_623fa4787cd146a18f4c9619",
    "x-app-key" : "nix_live_OsAL34vf1JJWrxQuqWtK5eLkgW11L7pN",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url = EXCERCISE_ENDPOINT, json = parameters, headers = headers)
result = response.json()
# print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = 'workout'
SHEET_ENDPOINT = "https://api.sheety.co/203a46583a7e9c27da9b9f9b1c9d6415/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)
    
    print(f"Sheety Response: \n {sheet_response.text}")