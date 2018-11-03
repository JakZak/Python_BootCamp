# ## 3. Stwórz klasę `Dog`
#
# Stwórz klasę `Dog` wedgług następującej specyfikacji:
#
# * pies zużywa energię szczekając (`bark`) i zyskuje śpiąc (`sleep`).
# * nowa instancja klasy `Dog` ma 10 jednostek energii
# * `Dog` ma metodę `sleep` która dodaje mu 2 jednostki energii
# * `Dog` ma metodę `bark` która konsumuje mu 1 jednostkę energii
# * `Dog` ma metodę `get_energy` która zwraca wartość energii instancji


# class dog:
#
#     energia = 0
#
#     def __init__(self,):
#         self.imie = imie
#         self.sleep.energia()
#         self.bark_energia()
#         self.stan = stan
#         self.energia = 10
#
#     def sleep(self):
#         self.stan = "Śpi"
#         self.sleep_energia()
#
#     def bark(self):
#         self.stan = "Szczeka"
#         self.bark.energia()
#
#     def get_energy(self):
#         self.energia
#
#     @classmethod
#     def sleep_energia(cls):
#         cls.energia += 2
#     def bark_energia(cls):
#         cls.energia -= 1
#     def energia(cls):
#         print(cls.energia)
#
# staszek = dog()
# filip = dog()
#
# print(staszek.get_energy)

#Rozwiazanie zajec

class dog:
    def __init__(self):
        self.energy = 10

    def slepp(self):
        self.energy += 2

    def bark(self):
        self.energy -= 1


def test_dog()
    assert dog.get_energy() == 10
    dog.bark()
    dog.bark()