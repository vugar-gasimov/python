import requests
from datetime import datetime
import json
USERNAME="vgasimov"
TOKEN="dsG6d1asGds1G5das5dH1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
CHESS_GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Chess Playing and Learning",
    "unit": "session",
    "type": "int",
    "color": "ajisai"
}

hearder = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=hearder)
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CHESS_GRAPH}"
today = datetime.now()
# If we want yesterday
# today = datetime(year=2024, month=6, day=15)
today = today.date().strftime("%Y%m%d")
print(today)
quantity = input("How many chess sessions did you do today?")
user_msg = input("What would you like to mention about your sessions?")
pixel_config = {
    "date": f"{today}",
    "quantity": quantity,
    "optionalData": json.dumps({
        "message": user_msg
    })
}
response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=hearder)
print(response.text)

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CHESS_GRAPH}/20240616"

update_config = {
    "quantity": "19",
    "optionalData": "{\"message\": \"Yesterday I did 19 chess sessions.\"}"
}
# response = requests.put(url=UPDATE_ENDPOINT, json=update_config, headers=hearder)
# print(response.text)


DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CHESS_GRAPH}/20240617"


# response = requests.delete(url=DELETE_ENDPOINT,  headers=hearder)
# print(response.text)