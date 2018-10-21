def plansza_gracz():
    from random import randint
    szerokosc = int(input("Wprowadź szerokość planszy [pix]:\n"))
    wysokosc = int(input("Wprowadź wysokość planszy [pix]:\n"))
    s_x = randint(0, szerokosc)
    s_y = randint(0, wysokosc)
    g_x = randint(0, szerokosc)
    g_y = randint(0, wysokosc)
    return g_x, g_y, szerokosc, wysokosc, s_x, s_y

def minimalna_liczba_krokow(s_x, s_y, g_x, g_y):
    min_kroki = abs(s_x - g_x) + abs(s_y - g_y)
    return min_kroki
mik = minimalna_liczba_krokow(s_x, s_y, g_x, g_y)

def ruch(s_x, s_y, g_x, g_y, min_kroki):
    if min_kroki != 0:
        print("Gdzie idziesz?")
        ruch = input()
        ruch = ruch.lower()
        if ruch == "w":
            g_y = g_y + 1
        if ruch == "s":
            g_y = g_y - 1
        if ruch == "a":
            g_x = g_x - 1
        if ruch == "d":
            g_x = g_x + 1
    return s_x, s_y, g_x, g_y

chodzenie

def po_ruchu(s_x, s_y, g_x, g_y, min_kroki):
    krok_po_ruchu = abs(s_x - g_x) + abs(s_y - g_y)
    if krok_po_ruchu < min_kroki:
        print("Idziesz w dobrym kierunku")
    if krok_po_ruchu > min_kroki:
        print("Nie tędy droga")
    if krok_po_ruchu == 0:
        print("Wygrałeś!!!")


# Plansza 10x10

from random import randint

s_x = randint(0, 10)  # Losowanie położenia skarbu

s_y = randint(0, 10)

print(s_x, s_y)

g_x = randint(0, 10)  # Losowanie położenia gracza

g_y = randint(0, 10)

print(g_x, g_y)

print('''Czas rozpocząć poszukiwania skarbu, możesz poruszać się w czterech kierunkach:
W - w górę
S - w dół
A - w lewo
D - w prawo
Powodzenia w znalezieniu skarbu.''')

# Obliczenie odległości x oraz y gracza od skarbu

min_kroki = abs(s_x - g_x) + abs(s_y - g_y)

while True:
    min_kroki = abs(s_x - g_x) + abs(s_y - g_y)
    if min_kroki != 0:
        print("Gdzie idziesz?")
        ruch = input()
        ruch = ruch.lower()
        if ruch == "w":
            g_y = g_y + 1
        if ruch == "s":
            g_y = g_y - 1
        if ruch == "a":
            g_x = g_x - 1
        if ruch == "d":
            g_x = g_x + 1
    krok_po_ruchu = abs(s_x - g_x) + abs(s_y - g_y)
    if krok_po_ruchu < min_kroki:
        print("Idziesz w dobrym kierunku")
    if krok_po_ruchu > min_kroki:
        print("Nie tędy droga")
    if krok_po_ruchu == 0:
        print("Wygrałeś!!!")
        break
