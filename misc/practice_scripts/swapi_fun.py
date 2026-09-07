import requests
import pandas as pd
import json

url = "https://swapi.py4e.com/api/planets/"

planets = []

while url is not None:
    response = requests.get(url)
    data = response.json()

    # Add all planets from the current page to the list
    planets.extend(data["results"])
    url = data["next"]

# response = requests.get(url)
# data = response.json()
# planets = data["results"]

# #print("Here is the results response:-", json.dumps(planets[0]["films"][0], indent=4))
# print("Film link:-", planets[0]["films"][0])
# url_film = planets[0]["films"][0]
# response_film = requests.get(url_film)
# data_film = response_film.json()
# print(data_film["title"])

planet_no = 1
for planet in planets:
    film_no = 1
    print (f"Planet {planet_no} : ", planet["name"])
    for film in planet["films"]:

        response_film = requests.get(film)
        data_film = response_film.json()
        print("Film numner:-", film_no , data_film["title"])
        
        film_no += 1
    print("-"*40)
    planet_no += 1