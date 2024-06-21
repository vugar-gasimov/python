import os
import requests
from dotenv import load_dotenv

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  
load_dotenv(dotenv_path)

URL_SHEETY = "https://api.sheety.co/5c1fc1796de51960f719832a5b44e251/flightDeals/prices"
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_header = {
            "Authorization": f"Bearer {SHEETY_AUTH}",
            "Content-Type": "application/json"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=URL_SHEETY, headers=self.sheety_header)
        if response.status_code == 200:
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)
            return []

    def update_iata_codes(self):
        for city in self.destination_data:
            update_data = {
                "price": {
                    "iataCode": city["iataCode"]  # Assuming city["iataCode"] holds the IATA code
                }
            }
            response = requests.put(url=f"{URL_SHEETY}/{city['id']}", json=update_data, headers=self.sheety_header)
            if response.status_code == 200:
                print(f"Row {city['id']} updated successfully.")
            else:
                print(f"Failed to update row {city['id']} with status code {response.status_code}")
                print(response.text)