#Ogarnac i dokonczyc bo raport nie dziala. Ewentualnie GIT Rafała

class Product:
    def __init__(self, id, name, price):
        self.ID = id
        self.name = name
        self.price = price

class Basket:

    def __init__(self):
        self.entries = []

    def __str__(self):
        return "Basket"

    def add_product(self, product, quantity):
        basket_entry = BasketEntry(product, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        sum_ = 0
        for e in self.entries:
            sum_ += e.count_price()
        return sum_

    def generate_report(self):
        total_price = self.count_total_price
        temp = ""
        for entry in self.entries:
            temp += entry.generate_report()
        output = '''Produkty w koszyku:
        {}W sumie{}
        '''
        return output.format(temp, total_price)

class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

    def generate_report(self):
        return f"""{self.product.name}({self.product.ID}), cena: {self.product.price} x {self.quantity}\n"""

def test_add_product_to_basket():
    basket = Basket()
    product = Product (1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1

def test_basket_count_total_price():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50

def test_basket_entry_count_price():
    be = BasketEntry(Product(1, "Woda", 2), 5)
    assert be.count_price() == 10

def test_basket_generate_report():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.generate_report() == '''Produkty w koszyku:
- Woda(1), cena: 10.00 x 5
W sumie: 50.0'''
