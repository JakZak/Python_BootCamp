import json

try:
    with open ("pracownicy.json") as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy = []

action = input ("co chcesz zrobic [d - dodaj, w - wypisz]: ")

if action == "d":
    imie = str(input("Imie: "))
    nazwisko = str(input("Nazwisko: "))
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja" : pensja,
    }
    pracownicy.append(pracownik)

    with open ("pracownicy.json", "w") as f:
        json.dump(pracownicy, f)

elif action == "w":
    print ("Pracownicy:")
    for i, pracownik in enumerate(pracownicy, start = 1):
        print (f"- [{i}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok urodzenia']}, pensja: {pracownik['pensja']} PLN ")



else:
    print ("Dokonano złego wyboru")