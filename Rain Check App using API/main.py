import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "04a57282ef6d22e5a6ed1186f530"
account_sid = "AC94cd190b9a0af8def7a2d53cda6a"
auth_token = "1fe99c7bac36f009d533a000c56"

weather_params = {
    "lat": 9.814305,
    "lon": -7.512570,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"][:4]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrealla.",
        from_="+122984364",
        to="+918930475",
    )
    print(message.status)