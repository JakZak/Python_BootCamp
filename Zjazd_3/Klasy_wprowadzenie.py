x = 1
napisz = "To jest napis"
y = 1.2
slownik = {}

print (type(x), type(napisz), type(slownik))

# instancja klasy int to (X), instancja klasy string to (napisz)

# Klasa
# instancja klasy
# metoda
# atrybuty

#definicja klasy
class Animal:#można ale nie trzeba dawaćnawiasów do klasy
    # pass
    # gatunek = "Canis Lupus"
    licznik = 0
    nazwa = "Fauna" # atrybut klasowy

    def __str__(self):
        return "Animal"
    def __init__(self, gatunek): #inicjalizujemy nowy obiekt/instancje z danymi do gatunku podczas wywolywania
        self.gatunek=gatunek #atrybut instancji
        self.zwieksz_licznik()
        self.stan = "nic nie robi"
        self.pasza = None

    def idz(self):
        self.stan = "idzie"

    def stoj(self):
        self.stan = "Stoi"

    def spij(self):
        self.stan = "Spij"

    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

#towrzenie obiektu danej klasy i jej instancji
azor = Animal("Canis Familiaris")
garfield = Animal("Felis catus")
rudolf = Animal("Rangifer tarandus")
print(azor)
# print(type(azor))
# print(dir(azor))
print(azor.gatunek)
print(rudolf.gatunek)#Wypisanie atrybutu

print(Animal.licznik)

garfield.idz()

print(garfield.stan)

garfield.spij()

print(garfield.stan)
print(azor.stan)

#DZIEDZICZENIE

class LeniweZwierzeta(Animal):

    def idz(self):
        self.stan = "Leży"
        print ("Chyba żartujesz")

print(dir(azor))
garfield = LeniweZwierzeta("Felis catus")
print(dir(garfield))
garfield.idz()
azor.idz()
# LeniweZwierzeta.idz(garfield)
print(garfield.stan)
print(azor.stan)