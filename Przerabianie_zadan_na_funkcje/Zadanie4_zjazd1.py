def naleznosc(cena, waga):
    return (cena * waga)

def paragon(cena, waga):
    return f"Kwota do zapłaty: {naleznosc(cena, waga)}"

def test_naleznosc():
    assert naleznosc(5, 2) == 10

def test_paragon():
    assert paragon(5 ,2) == "Kwota do zapłaty: 10"


