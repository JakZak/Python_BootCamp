import modulo as modulo

liczba = int(input ("Podaj liczbę do sprawdzenia: "))

output = f"""Większa od 10: {liczba>10}
Mniejsza lub równa 15: {liczba<=15}
Podzielna przez 2: {liczba%2==0}"""
print(output)

#opcja 2

a=liczba>10
b=liczba<=15
c=liczba%2==0

output2 = f"""Większa od 10: {a}
Mniejsza lub równa 15: {b}
Podzielna przez 2: {c}"""
print(output2)

#