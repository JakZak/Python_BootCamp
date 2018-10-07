print("Program obliczy średnią temperaturę")
print("Podaj wartości temperatury dla których chcesz obliczyć średnią i na koniec wpisz 'oblicz' ")

LICZBA_DNI_TYGODNIA = 7
numer_dnia = 1
suma_temperatur = 0

min_ = None
max_ = None
while numer_dnia <= LICZBA_DNI_TYGODNIA:
    temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}: "))
    suma_temperatur += temp
    if numer_dnia == 1:
        min_ = temp
        max_ = temp
    else:
        if temp < min_:
            min_ = temp
        if temp > max_:
            max_ = temp
    numer_dnia += 1
srednia_temperatur = int(suma_temperatur / LICZBA_DNI_TYGODNIA)

print(srednia_temperatur)
print(min_, max_)





