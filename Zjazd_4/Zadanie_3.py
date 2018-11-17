import json

import urllib.request

import sys

from collections import namedtuple


# lokalizacja = input ("Podaj lokalizację dla której chcesz sprawdzić pogodę w języku angielskim: ")
#
# with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={lokalizacja}") as f:
#     print(f)
#     id = json.loads(f.read())
#
# for i in id:
#     lokalizacja = i['woeid']
#     print(lokalizacja)
#
# with urllib.request.urlopen(f"https://www.metaweather.com/api/location/{lokalizacja}") as f:
#     print(f)
#     pogoda = json.loads(f.read())
#     print(pogoda)
Weather = namedtuple()

def get_location_id(location_name):
    url = f"https://www.metaweather.com/api/location/search/?query={location_name}"
    with urllib.request.urlopen (url) as f:
        result = json.loads(f.read())
        return result[0]['woeid']

def get_location_weather(location_id):
    url = f"https://www.metaweather.com/api/location/{location_id}"
    with urllib.request.urlopen(url) as f:
        result = json.loads(f.read())
        return result


if __name__ == "__main__":
    location_id = get_location_id(sys.argv[1])
    print(location_id)
    weather = get_location_weather(location_id)
    print(weather)

