import requests

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "e39ee804f"
CITY_NAME="Krakow"
COUNTRY = "Poland"
CITY_LAT= 50.064651
CITY_LON= 19.944981

parameters = {
    "lat": CITY_LAT,
    "lon": CITY_LON,
    "appid": API_KEY
}
response = requests.get(url=URL, params=parameters)

print(response.status_code)
print(response.raise_for_status())
response.raise_for_status()

weather_data = response.json()
weather_details = []
# every id and description
for data in weather_data["list"]:
    
    weather_info = data["weather"][0]
    weather_id = weather_info["id"]
    weather_desc = weather_info["description"]
    # weather_id = weather_data["list"]["weather"]["id"]
    # print(weather_id)
    # weather_desc = weather_data["list"]["weather"]["description"]
    # print(weather_desc)
    weather_details.append({'id': weather_id, 'description': weather_desc})
print(weather_details)