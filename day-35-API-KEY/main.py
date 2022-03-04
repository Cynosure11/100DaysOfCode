import requests
import os
from twilio.rest import Client

# ОШИБКА НАХУЙ БЛЕТЬ!


os.environ_1 = "ACfd668f713292bb8a2a9e8106a14128d9"
account_sid = os.environ
os.environ = "c0e36b81040cf2876e344cefb27e984b"
auth_token = os.environ


OWM_Ednpoint = "https://api.openweathermap.org/data/2.5/onecall"
# API_KEY gotten from home.openweathermap.org/api_keys
api_key ="ad4e165aa9ba0ecb81a261dccc6b75d8"
PART = "current"

weather_params= {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Ednpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='Its going to rain today. Remember to bring an umbrella ☔️',
        from_='+18647635134',
        to='+15083678279'
    )

    print(message)

# print(weather_data["hourly"][0]["weather"][0]["id"])



