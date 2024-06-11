import requests 
from datetime import datetime 

URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 50.450100
MY_LNG = 30.523399

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise.split("T")[0], sunrise.split("T")[1].split(":")[0], sunset.split("T"))
print(sunrise, sunset)

time_now = datetime.now()

print(time_now.hour)

