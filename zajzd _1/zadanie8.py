print("Cześć, podaj wymiary opakowania w podanej kolejności: wysokość, szerokość, długość.")
wysokosc = float(input("Wysokość: "))
szerokosc = float(input("Szerokość: "))
dlugosc = float(input("Długość: "))

objetosc = int(wysokosc * szerokosc * dlugosc)

if objetosc > 1000:
    print("Objetość opakowania jest większa niż 1 L i spełnia wymagania")
else:
    print("Niestety twoje opakowanie jest za małe, znajdź większe :)")