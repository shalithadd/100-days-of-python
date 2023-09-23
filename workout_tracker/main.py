import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv('.env')
app_id = os.getenv('APP_ID_NUTRITIONIX')
api_key = os.getenv('APIKEY_NUTRITIONIX')
nutritionix_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'

add_row_endpoint = 'https://api.sheety.co/52d0e86a43ac5f22aa892f89acbb9d94/myWorkouts/workouts'
token = os.getenv('SHEETY_TOKEN')


def get_exercise_data():
    headers = {
        'x-app-id': app_id,
        'x-app-key': api_key
    }
    request_body = {
        'query': input('What exercise did you do? '),
        'gender': 'male',
        'weight_kg': 50.5,
        'height_cm': 161,
        'age': 33,
    }

    response = requests.post(url=nutritionix_end_point, json=request_body, headers=headers)
    return response.json()


def post_exercise_data(result):
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M:%S')

    for exercise in result["exercises"]:
        sheet_data = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': exercise['name'].title(),
                'duration': exercise["duration_min"],
                'calories': exercise["nf_calories"],
            }
        }

    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(url=add_row_endpoint, json=sheet_data, headers=headers)
    print(response.text)


post_exercise_data(get_exercise_data())


