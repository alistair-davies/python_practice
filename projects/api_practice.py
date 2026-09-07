#JSON and API Practice
#Get information from a webpage on star wars stats
import requests
import pandas as pd


planets = []
url = "https://swapi.py4e.com/api/planets/"

while url is not None:
    response = requests.get(url)
    data = response.json()

    # Add all planets from this page
    planets.extend(data["results"])

    # Move to the next page
    url = data["next"]

for planet in planets:
    resident_urls = planet["residents"]
    resident_data = []

    for r in resident_urls:
        res = requests.get(r).json()
        resident_data.append(res["name"])

    planet["resident_names"] = resident_data


df = pd.DataFrame(planets)
print(df.head())
print(len(df))
print(df["name"].sort_values().to_string(index=False))
#print(df["name"].sort_values().reset_index(drop=True))

ends_with_th = df["name"].str.endswith("th").sum()
ends_with_er = df["name"].str.endswith("er").sum()

print("Planets ending with 'th':", ends_with_th)
print("Planets ending with 'er':", ends_with_er)

# Take just the first 3 planets
sample_planets = planets[:3]

for planet in sample_planets:
    print("Planet:", planet["name"])
    print("Original resident URLs:", planet["residents"])

    resident_urls = planet["residents"]
    resident_data = []

    for r in resident_urls:
        res = requests.get(r).json()
        resident_data.append(res["name"])

    planet["resident_data"] = resident_data

    print("Resident names:", planet["resident_names"])
    print("-" * 40)

