def pole_trapezu(a, b, c):
    return (((a + b)*c)/2)


def test_pole_trapezu():
    assert pole_trapezu(3, 9, 6.5) == 39.0
