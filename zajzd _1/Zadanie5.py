#KOszty spalania przejazdu z miasta jednego do drugiego

miasto_a = input("Podaj miasto startowe: ")
miasto_b = input("Podaj miasto docelowe: ")
dystans = float(input("Podaj ilość kilometrów: "))
cena_paliwa = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Podaj spalanie: "))

koszt_100 = spalanie*cena_paliwa

koszt_km = koszt_100/100

koszt_przejazdu = int(koszt_km * dystans)

print(miasto_a, miasto_b, dystans, cena_paliwa, spalanie, sep="\n")
print(f"Całkowity koszt przejazdu z {miasto_a} do {miasto_b} wynosi: {koszt_przejazdu}")

