def pobieranie_danych():
    miasto_a = input("Podaj miasto startowe: ")
    miasto_b = input("Podaj miasto docelowe: ")
    dystans = float(input("Podaj ilość kilometrów: "))
    cena_paliwa = float(input("Podaj cenę paliwa: "))
    spalanie = float(input("Podaj spalanie: "))
    return miasto_a, miasto_b, dystans, cena_paliwa, spalanie

def koszt_przejazdu (miasto_a, miasto_b, dystans, cena_paliwa, spalanie):
    koszt = int((dystans / 100) * spalanie * cena_paliwa)
    return koszt
# def drukuj(miasto_a, miasto_b, dystans, cena_paliwa, spalanie,):
#     return (f"Całkowity koszt przejazdu z {miasto_a} do {miasto_b} wynosi: {koszt_przejazdu(koszt_przejazdu)}")

def kalkulacja():
    dane = pobieranie_danych()
    oplata = koszt_przejazdu(*dane)
    print(f"Całkowity koszt przejadu to: {oplata}")

kalkulacja()






