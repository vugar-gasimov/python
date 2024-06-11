import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(requests.__version__)

print(response.status_code)
# if response.status_code != 200:
#     raise Exception("Bad response from iss api.")
response.raise_for_status()

data = response.json()
# data = response.json()["iss_position"]
# data = response.json()["iss_position"]["latitude"]
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (longitude, latitude )
print(data)
print(iss_position)