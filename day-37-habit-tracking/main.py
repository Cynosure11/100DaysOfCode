# Pixela - Its tracking your habits, how many pages you was read
# Get - requests.get()
# Post - requests.post(
# Put - requests.put()
# Delete - requests.delete()
import requests
from datetime import datetime

TOKEN = "ayaalatlasov1996"
USERNAME = "ayaal2022"
GRAPH_ID = "mygraph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=2, day=23)
# print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "24",
}

# response2 = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
# print(response2.text)


# If you wanna change current information
# Use REQUESTS.PUT()
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_update_data = {
    "date": "20220223",
    "quantity": "54",
}

# response3 = requests.put(url=update_endpoint, headers=headers, json=new_update_data)
# print(response3.text)


# Delete your pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response4 = requests.delete(url=delete_endpoint, headers=headers)
print(response4.text)

