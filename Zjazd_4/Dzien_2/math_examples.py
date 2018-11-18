import math


class Kula:
    def __init__(self, r):
        self.promien = r

    def objetosc(self):
        return (4/3) * math.pi * math.pow(self.promien, 3)

    def surface(self):
        return 4 * math.pi* self.promien ** 2

s = Kula(10)
print(s.objetosc())
print(s.surface())