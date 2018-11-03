class ElectricCar:

    def __init__(self, zasieg):
        self.zasieg = zasieg
        self.left = zasieg

    def drive(self, dystans):
        self.left = self.zasieg - dystans
        if self.left <= 0:
            return self.left
        return self.left

    def charge(self):
        self.left = self.zasieg
        return self.left


def test_car():
    car = ElectricCar(100)
    assert car.drive(70) == 30
    assert car.drive(50) == 50
    assert car.drive(30) == 70
    assert car.charge() == 100
    assert car.drive(100) == 0

def test_car_dwa():
    car2 = ElectricCar(200)
    assert car2.drive(70) == 130
    assert car2.drive(50) == 150
    assert car2.drive(30) == 170
    assert car2.charge() == 200
    assert car2.drive(200) == 0
    