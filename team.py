import requests
from config import API_KEY_SPORT

url = f"https://v2.nba.api-sports.io/teams"
headers = {
        'x-rapidapi-key': API_KEY_SPORT,
        'x-rapidapi-host': 'v2.nba.api-sports.io'
        }

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for i in range(data['results']):
        print(f"{data['response'][i]['id']}  -  {data['response'][i]['name']}")
