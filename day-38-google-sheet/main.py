# Python Datetime strftime()
# APIs and making POST requests - requests.post()
# Authorization Headers
# Environment Variables
import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 170
AGE = 25
APP_ID = os.environ["cd0b0d07"]
API_KEY = os.environ["08c9508f1811d40a47853af9866c0558"]

endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients/"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
user_params = {
    "query": "1 large banana bread",
}
# response = requests.post(url=endpoint, headers=headers, json=user_params)
# print(response.text)
today = datetime(year=2022, month=2, day=23)
SHEETY_ENDPOINT = "https://api.sheety.co/f307a8432a8f684c4259bee0564ecb90/myfirstproject/workouts"
workout = {
    "date": today.strftime("%Y%m%d"),
    "time": "15:00:00",
    "exercise": "Eating",
    "duration": 10,
    "calories": 130,
    "id": 2
}


response = requests.post(url=SHEETY_ENDPOINT, json=workout)
print(response.json)


