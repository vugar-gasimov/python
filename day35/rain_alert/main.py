import requests
from twilio.rest import Client
# import os
# To use twillio with python anywhere
# from twilio.http.http_client import TwilioHttpClient
#after if proxy_client = TwilioHttpClient()
# and than proxy_client.session.proxies = {'https': os.version['https_proxy']}
# last step client = Client(account_sid, auth_token, http_client = proxy_client)
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "e39ee804f42c5fa"
CITY_NAME="Krakow"
COUNTRY = "Poland"
CITY_LAT= 50.064651
CITY_LON= 19.944981
LIMITATION = 4

account_sid = ''
auth_token = ''

# client = Client(account_sid, auth_token)
parameters = {
    "lat": CITY_LAT,
    "lon": CITY_LON,
    "cnt": LIMITATION,
    "appid": API_KEY
}
response = requests.get(url=URL, params=parameters)

# print(response.status_code)
# print(response.raise_for_status())
response.raise_for_status()

weather_data = response.json()
weather_details = []
will_rain = False
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
# print(weather_details)

rain_msg = "It's gonna rain, don't forget your umbrella at home."

for detail in weather_details:
    if detail["id"] < 700:
        # print(f"{rain_msg} Forecaster message: {detail['description']}")
        will_rain = True
    # else:
        # print(f"Short rain break, Forecaster message: {detail['description']}")
        
if will_rain:
    # print("Bring umbrella.")
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    # body=f"{rain_msg} Forecaster message: {detail['description']} ☂️.",
    # from_='+18038642107',
    # to='+380'
    # # to='Your verified number'
    # )
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"{rain_msg} Forecaster message: {detail['description']} ☂️.",
    to='whatsapp:+380'
    )
    print(message.sid)
else:
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    # body=f"{rain_msg} Forecaster message: {detail['description']} ☂️.",
    # from_='+18038642107',
    # to='+380'
    # # to='Your verified number'
    # )
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"Today it will not rain, Forecaster message: {detail['description']}. ",
    to='whatsapp:+380'
    )
    print(message.sid)
  
    # print(message.status)