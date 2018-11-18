import json
import urllib.request
import sys
from collections import namedtuple

Weather = namedtuple("Weather", ["location", "temperature", "air_pressure", "humidity"])

def get_location_id(location_name):
    url = f"https://www.metaweather.com/api/location/search/?query={location_name}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read())
        if results:
            return results[0]['woeid']


def get_location_weather(location_id):
    url = f"https://www.metaweather.com/api/location/{location_id}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read())

        location = results['title']
        temp = results['consolidated_weather'][0]['the_temp']
        humidity = results['consolidated_weather'][0]['humidity']
        air_pressure = results['consolidated_weather'][0]['air_pressure']

        weather = Weather(location, temp, air_pressure, humidity)
        return weather

def print_weather(weather):
    print(f"""
Pogoda w lokalizacji: {weather.location}
 - Temperatura: {weather.temperature}
 - Ciśnienie: {weather.air_pressure}
 - Wilgotność: {weather.humidity}
 """)


if __name__ == "__main__":
    # pobrać id dla lokalizacji
    location_id = get_location_id(sys.argv[1])
    # pobrać pogodę dla lokalizacji
    weather = get_location_weather(location_id)
    print(weather[0])
    print(weather.location)
    # wyświetlić wynik
    print_weather(weather)

import tkinter

def pogoda():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik.configure(text = a + b)

root = tkinter.Tk()

miasto_label = tkinter.Label(master=root, text = "Miasto")
miasto_label.pack()
miasto_entry = tkinter.Entry(master=root)
miasto_entry.pack()

b_label = tkinter.Label(master=root, text = "Parametr b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

wynik_label = tkinter.Label(master=root, text = "Wynik")
wynik_label.pack()

wynik = tkinter.Label(master=root, text = " - ")
wynik.pack()

policz_button = tkinter.Button(master = root, text = "Policz", command = get_location_weather)

policz_button.pack()





root.title("Sumator")
root.mainloop()