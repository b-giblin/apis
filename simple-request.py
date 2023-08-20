from urllib import response
import requests
import json

r = requests.get("https://api.chucknorris.io/jokes/random")

r = r.json()
punchline = r["value"]

print(f"I have a good joke for you... {punchline}")
