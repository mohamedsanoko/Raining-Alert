import requests
from twilio.rest import Client
import os

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = "+15412486181"
MY_LAT = "45.5031824"
MY_LONG = "-73.5698065"

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API_KEY,
    "cnt": 4
}

weather_response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

will_rain = False
for weather in weather_data['list']:
    weather_id = weather['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It is going to rain today. Remember to bring an ☂️.",
            from_=TWILIO_PHONE_NUMBER,
            to='+14383345118'
        )
    print(message.status)


