# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie,
# #  np.: HELLO STRANGER! ->
# # H L O S R N E !
# #  E L   T A G R

def wczystaj_tekst():
    tekst = input("Podaj tekst do wyświetlenia: ")
    return tekst
def wyswietlanie_naprzemienne(tekst):
    linia1 = tekst[::2]
    linia2 = tekst [1::2]
    print(linia1)
    print(linia2)

tekst = wczystaj_tekst()
wyswietlanie_naprzemienne(tekst)




