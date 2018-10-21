# Napisz program, który wczyta od użytkownika tekst, a następnie podwoi w nim co drugi znak i wyświetli wynik,
#
# np.: ALA MA PSA -> ALLA  MAA PPSAA

def podanie_tekstu():
    tekst = input ("Podaj tekst do podwojenia: ")
    return tekst

def podwajanie_liter(tekst):
    pojedyncze = tekst[0::2]
    podwojone = tekst [1:2]
    for znak in pojedyncze:
        a = znak
    for znaki in podwojone:
        b = znaki

print(podwajanie_liter ('kuba'))