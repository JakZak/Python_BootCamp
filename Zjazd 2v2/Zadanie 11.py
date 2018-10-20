liczby = set()
print(dir(liczby))
while True:
    komenda = input("Wpisz liczbę lub [z] aby zakończyć\n")
    if komenda == "z":
        break
    if komenda ==" ":
        break
    komenda
    liczby.add(int(komenda))

zbior_dodatni = set(range(0, 101, 2))
wynik = zbior_dodatni&liczby
ile_wynik = len(wynik)
unikaty = len(liczby)

print(f" Wpisałeś {unikaty} unikatowych cyfr/liczb z czego {ile_wynik} to liczby parzyste w zakresie od 0 - 100")

