print("Program obliczy średnią z wprowadzonych wartości")
print("Po wpisaniu wszystkich wartości naciśniej 'ENTER'")

numer = 1
suma = 0
liczba = None

min_ = None
max_ = None

while True:
    liczba = input(f"Podaj wartość numer {numer}: ")
    if liczba == "":
        print("Liczę średnią, min, max, mediane i inne pierdoły")
        numer-=1
        break
    liczba = float(liczba)
    if min_ == None or liczba < min_:
        min_ = liczba
    if max_ == None or liczba > max_:
        max_ = liczba
    suma += float(liczba)
    srednia = suma / numer
    numer += 1

output = f"""Oto twoje wyniki:
Suma = {suma}
Ilość wprowadzonych danych = {numer}
Średnia = {srednia}
Min = {min_}
Max = {max_}
"""

print (output)