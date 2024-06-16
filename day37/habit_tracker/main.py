import requests

USERNAME="vgasimov"
TOKEN="dsG6d1asGds1G5das5dH1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

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

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=hearder)
print(response.text)