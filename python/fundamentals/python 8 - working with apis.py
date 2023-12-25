import requests

astro_request = requests.get('http://api.open-notify.org/astros.json')
astro_url = 'http://api.open-notify.org/astros.json'
astro_request = requests.get(astro_url)
type(astro_request)

astro_request.status_code
astro_request.json()
astro_json = astro_request.json()
astro_json
type(astro_json)

astro_json.keys()
astro_json['people']
astro_json['people'][0]['name']

dad_joke_url = 'https://icanhazdadjoke.com'
dad_joke_request = requests.get(
    url=dad_joke_url,
    headers={'Accept': 'application/json'})

dad_joke_request.status_code
dad_joke_json = dad_joke_request.json()
dad_joke = dad_joke_json
print(dad_joke)

import requests
def ten_apis(url):
    output = []
    for i in range(0, 10):
        api_request = requests.get(url, headers={'Accept': 'application/json'})
        if api_request.status_code == 200:
            output.append(api_request.json()['joke'])
        else:
            output = f'Error code {api_request.status_code}'
    return output

ten_apis('https://icanhazdadjoke.com')

import requests
def ten_apis(url):
    output = ['0']
    char_count = 0
    for i in range(0, 10):
        api_request = requests.get(url, headers={'Accept': 'application/json'})
        if api_request.status_code == 200:
            if len(api_request.json()['joke']) > char_count:
                char_count = len(api_request.json()['joke'])
                output[0] = api_request.json()['joke']
        else:
            output = f'Error code {api_request.status_code}'
    output.append(f'Joke length = {char_count}')
    return output

ten_apis('https://icanhazdadjoke.com')

star_wars_root = 'https://swapi.dev/api/'
star_wars_result = requests.get(star_wars_root)
star_wars_result.raise_for_status()
star_wars_request.status_code

star_wars_json = star_wars_result.json()
vehicles_json = requests.get('https://swapi.dev/api/vehicles/').json()
vehicles_json

type(vehicles_json['results'])
vehicles_json['count']
len(vehicles_json['results'])

import pandas as pd

vehicles = pd.DataFrame(vehicles_json['results'])
vehicles.head()

requests.get('https://swapi.dev/api/vehicles?search=Sand').json()
species_url = 'https://swapi.dev/api/species'
species_result = requests.get(species_url)
species_result.raise_for_status()

species_json = species_result.json()
species_json

sw_species = pd.DataFrame(species_json['results'])
sw_species
sw_species.shape

species_json['next']

import math
import requests
import pandas as pd

def url_to_df(url):
    output = []
    api_request = requests.get(url)
    api_json = api_request.json()
    count = api_json['count']
    for i in range(0, math.ceil((count) / 10)):
        api_request = requests.get(url)
        if api_request.status_code == 200:
            output.extend(api_request.json()['results'])
            url = api_json['next']
        else:
            output = f'Error code {api_request.status_code}'
    df = pd.DataFrame(output)
    return df

url_to_df('https://swapi.dev/api/people/')

url = "https://api.tfl.gov.uk/Line/Mode/tube/Disruption"
API_KEY = "9a2f4ecaa64743b8a2ce3275ba5bab2f"
tfl = requests.get(f"{url}?app_key={API_KEY}")

print(tfl.status_code)
tfl.json()

API_KEY = "9a2f4ecaa64743b8a2ce3275ba5bab2f"
disruptions = requests.get(f'https://api.tfl.gov.uk/Disruptions/Lifts?app_key={API_KEY}')
disruptions.raise_for_status()

disruptions.json()
len(disruptions.json())

outcome = []
year = 2017
for i in range(3):
    accidents = requests.get(f'https://api.tfl.gov.uk/AccidentStats/{year}?app_key={API_KEY}')
    outcome.extend(accidents.json())
    print(f'In {year} there were {len(accidents.json())} accidents')
    year += 1

bike_points =- requests.get(f'https://api.tfl.gov.uk/BikePoint/Search?query=Hyde Park&app_key={API_KEY}')
bike_points.json()

stationid = 'victoria'
url = f'https://api.tfl.gov.uk/Line/{stationid}/StopPoints'

stations = requests.get(f'{url}?app_key={API_KEY}')
stations.json()