import requests
import json

location = input("Provide a location to see its weather:  ")
params = {
    "access_key": "0aa657bcf59649d231be4ed17ed0ecbe",
    "query": location,
    "units": "f",
}


api_result = requests.get("http://api.weatherstack.com/current", params)
api_response = api_result.json()
current_temp = api_response["current"]["temperature"]
location_name = api_response["location"]["name"]


print(f"The current tempurature in {location_name} is {current_temp}\xb0 F")
