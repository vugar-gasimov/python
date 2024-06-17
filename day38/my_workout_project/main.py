import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  
load_dotenv(dotenv_path)

APP_ID = os.getenv('APP_ID')
API_KEY =  os.getenv('API_KEY')
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
URL_SHEETY = "https://api.sheety.co/5c1fc1796de51960f719832a5b44e251/myWorkouts/workouts"
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

GENDER = "male"
WEIGHT_KG = 94    
HEIGHT_CM = 183  
AGE = 26

now = datetime.now()
today_date = now.strftime("%Y/%m/%d")
today_time = now.strftime("%H:%M:%S")

user_input = input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": 0, 
}

# exercise_payload = {
#     "query": user_input
# }
exercise_payload = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# bearer_headers = {
# "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     headers=bearer_headers
# )

sheety_headers = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}

response = requests.post(url=URL, json=exercise_payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    for exercise in data["exercises"]:
        exercise_name = exercise["name"].title() 
        duration = exercise["duration_min"]
        calories = exercise["nf_calories"]
        
        sheety_config = {
            "workout": {
                "date": today_date,
                "time":today_time,
                "exercise": exercise_name,
                "duration": duration,
                "calories": calories,
            }
        }
    
        sheety_response = requests.post(url=URL_SHEETY, json=sheety_config, headers=sheety_headers)
    
        if sheety_response.status_code == 200:
            print(f"Workout {exercise_name} logged successfully.")
        else:
            print(f"Failed to log workout {exercise_name} with status code {sheety_response.status_code}")
            print(sheety_response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
    

sheety_check_response = requests.get(url=URL_SHEETY, headers=sheety_headers)

if sheety_check_response.status_code == 200:
    print("Sheety API is working properly.")
    sheety_data = sheety_check_response.json()
    # print(json.dumps(sheety_data, indent=4))  
    
    def pretty_print_workouts(data):
        for workout in data['workouts']:
            print(f"Date: {workout['date']}")
            print(f"Time: {workout['time']}")
            print(f"Exercise: {workout['exercise']}")
            print(f"Duration: {workout['duration']} minutes")
            print(f"Calories: {workout['calories']}")
            print(f"ID: {workout['id']}")
            print("-" * 40)


    pretty_print_workouts(sheety_data)
else:
    print(f"Failed to access Sheety API with status code {sheety_check_response.status_code}")
    print(sheety_check_response.text)