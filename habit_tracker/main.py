import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv('.env')
pixela_endpoint = 'https://pixe.la/v1/users'
token = os.getenv('TOKEN')
user_name = os.getenv('USER_NAME')

user_params = {
    'token': token,
    'username': user_name,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{user_name}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'hours',
    'type': 'float',
    'color': 'sora',
}

headers = {'X-USER-TOKEN': token}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_create_endpoint = f'{graph_endpoint}/graph1'
today = datetime.now()
day = today.strftime('%Y%m%d')
pixel_params = {
    'date': day,
    'quantity': input('How many hours did you code today? '),
}

response = requests.post(url=pixel_create_endpoint, json=pixel_params, headers=headers)
print(response.text)

pixel_edit_endpoint = f'{pixel_create_endpoint}/{day}'
pixel_edit_params = {'quantity': '10.5'}

# response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f'{pixel_create_endpoint}/{day}'

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
