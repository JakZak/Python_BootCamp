# #dodawanie
# #odejmowanie
# rownosc
# mniejsze niz
# mnozenie (przez skale)

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        vector = (self.x, self.y)

    def __add__(self, other):#dodawanie
        x = self.x + other.x
        y = self.y + other.y
        vector = (x, y)
        return vector

    def __sub__(self, other):#odejmowanie
        x = self.x - other.x
        y = self.y - other.y
        vector = (x, y)
        return vector

    def __eq__(self, other):#rownosc
        x = self.x == other.x
        y = self.y == other.y
        return x == y

    def __mul__(self, other):#mnozenie
        x = self.x * other.x
        y = self.y * other.y
        vector = (x, y)
        return vector

    def __lt__(self, other):#mniejsze
        x = self.x < other.x
        y = self.y < other.y
        return x == y

    def lenght_vector(self):
        return (self.x**2 + self.y**2)**(0.5)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TESTY<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def test_vector_dodawanie():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(1, 2)
    assert vector_1 + vector_2 == (2, 4)

def test_vector_odejmowanie():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(1, 2)
    assert vector_1 - vector_2 == (0, 0)

def test_vector_mnozenie():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(1, 2)
    assert vector_1 * vector_2 == (1, 4)

def test_vector_mnozenie_przez_skale():
    vector_1 = Vector(2, 4)
    result = vector_1 * 2

    assert result.x == 4
    assert result.y == 8

def test_vector_rownosc():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(1, 2)
    assert vector_1 == vector_2

def test_vector_mniejszy_niz():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(1, 2)
    assert vector_1 < vector_2

def test_lenght_vector():
    vector = Vector(2, 2)
    assert vector.lenght_vector() == 8**0.5
