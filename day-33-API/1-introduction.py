# What is API - Application Programming Interface
# is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with
# an external system

# (request) My program -> API -> External System and
# then Data (response) from External System -> API -> My Data

# Download extension "JSON viewer awesome"

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)


# HTTPS Response Codes httpstatuses.com
# 1xx Hold on - Loading
# 2xx Here you go - Success
# 3xx Go Away
# 4xx You Screwed Up - Error, 404 - page is not found
# 5xx I Screwed Up