
class Product:

    def __init__(self, ID, nazwa, cena):
        self.nazwa = nazwa
        self.ID = ID
        self.cena = cena

    def print_info(self):
        return f'Produkt "{self.nazwa}", ID: {self.ID}, cena: {self.cena} PLN'


def test_pruduct():
    product = Product(1, 'Woda', 10.99)
    assert product.ID == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99

def test_product_print_info():
    product = Product(1, 'Woda', 10.99)
    assert product.print_info() == 'Produkt "Woda", ID: 1, cena: 10.99 PLN'