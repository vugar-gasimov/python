import os
import requests
from dotenv import load_dotenv

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  
load_dotenv(dotenv_path)

class FlightSearch:
    
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self.get_new_token()
        
    def get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret 
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=data)
        
        if response.status_code == 200:
            token_data = response.json()
            print(f"Your token is {token_data['access_token']}")
            print(f"Your token expires in {token_data['expires_in']} seconds")
            return token_data['access_token']
        else:
            print(f"Failed to obtain token. Status code: {response.status_code}")
            print(response.text)
            return None
        
    def search_city(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError, 
        or "Not Found" if no match is found due to a KeyError.
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "subType": "CITY",
            "keyword": city_name,
            "max": 1
        }
        response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Failed to search city. Status code: {response.status_code}")
            print(response.text)
            return "N/A"
        
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            print(f"No airport code found for {city_name}.")
            return "N/A"

        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Searches for flight options between two cities on specified departure and return dates
        using the Amadeus API.
        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.
        Returns:
            dict or None: A dictionary containing flight offer data if the query is successful; None
            if there is an error.
        The function constructs a query with the flight search parameters and sends a GET request to
        the API. It handles the response, checking the status code and parsing the JSON data if the
        request is successful. If the response status code is not 200, it logs an error message and
        provides a link to the API documentation for status code details.
        """

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"Failed to check flights. Status code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                "For details on status codes, check the API documentation:\n"
                "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                "-reference")
            print("Response body:", response.text)
            return None
        return response.json()