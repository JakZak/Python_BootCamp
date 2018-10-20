#Uporządkować

# produkty = {"ziemniaki": 2.00, "ketchup": 2.65, "woda": 1.99}
# # dodac kod wyświetlajacy
#
# for p in produkty.items():
#     name, cena = p
#     print(f"{name} - {cena} PLN")
#
# produkt = input("Podaj nazwę produktu: ")
#
# ile = float(input("Podaj masę towaru (w 'kg') lub ilość sztuk: "))
#
# a = None
# cena = 0
# if produkt in produkty:
#     a = produkty[produkt]
#     cena = ile * a
# print(cena)

# Wykonanie prowadzącego
produkty = {"ziemniaki": 2.00, "ketchup": 2.65, "woda": 1.99}
magazyn = {"ziemniaki": 10, "ketchup": 25, "woda": 40}

#Wykonanie wielu zakupów:
while True:
    for produkt in produkty:
        print(f" {produkt} - {produkty[produkt]} PLN ")
    komenda = input("Co chcesz zrobic: [k]upic, [koniec] by przerwać zakupy, dodać zakup [d]odac")
    if komenda == 'koniec':
        break
    if komenda == "k":
        produkt = input("Podaj nazwę produktu: ")
        ile = float(input("Podaj masę towaru (w 'kg') lub ilość sztuk: "))
        if produkt not in produkty:
            print('Nie mamy takieg produktu!')
            continue
        if produkt in produkty:
            a = produkty[produkt]
            cena = ile * a
            if produkt in magazyn:
                zakup = magazyn[produkt]
                magazyn[produkt] = zakup - ile
            for produkt in magazyn:
                print(f" Stan magazynu: {produkt}, {magazyn[produkt]}")
        if magazyn[produkt] < ile:
            print("mamy za mało towaru")
    elif komenda == "d":
        produkt_dodany = input("Jaki produkt chcesz dodać?\n")
        ilosc_dodana = int(input("Ile produktu dodać?\n"))
        if produkt_dodany not in magazyn:
            magazyn[produkt_dodany] = ilosc_dodana
            cena_nowego_produktu = input("Podaj cenęnowego produktu:\n ")
            produkty[produkt_dodany] = cena_nowego_produktu
            print(magazyn)
        elif produkt_dodany in magazyn:
            magazyn[produkt_dodany] += ilosc_dodana
    else:
        print('Niepoprawna komenda')
rachunek = 0
rachunek += cena
print(int(rachunek))
