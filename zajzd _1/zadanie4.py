cena_kg = 10.0
waga = 2.5
naleznosc = 25.0

kwota = cena_kg * waga
print (kwota)

output = f"""Cena za kilogram: {cena_kg}
Waga: {waga}
Należność: {naleznosc}"""
print (output)

#dodatek
if kwota==naleznosc:
    print ("Dziękuję")
else:
    print("Kwota się nie zgadza")