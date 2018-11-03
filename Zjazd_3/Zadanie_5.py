class Product:
    def __init__(self, ID, nazwa, cena):
        self.nazwa = nazwa
        self.ID = ID
        self.cena = cena

class Basket:

    def __init__(self, ID, nazwa, cena):
        super().__init__(ID, nazwa, cena)
        self.produkty = []
    def add_product(self):
        pass

    def count_total_price(self):
        self.total_price = Product.cena * ilosc

    def generate_raport(self):
        pass


def test_basket():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50


# basket.generate_raport()
# '''Produkty w kosztyku
# - Woda (1), cena: 10.00 x 5
# W sumie: 50.00'''
