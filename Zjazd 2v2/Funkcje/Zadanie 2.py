napis = "kubasasasdfdsf"
napis = napis.lower

def wiecej_niz(napis, prog):
    litery = {}
    wynik = set()
    for litera in napis:
        litery[litera] = litery.get(litera, 0) +1
    for key, value in litery.items():
        if value > prog:
            wynik.add(key)
    print(wynik)

wiecej_niz('sadasdadasdaffdfdf', 3)



#TETSY
def tets_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz(", 0") == set()
def test_wiecej_niz_dla_nie_pustego_napisu():
    assert wiecej_niz("aaaaabbbbbccccdfg", 4) == {'a', 'b'}
#

#roywiayanie prowadyacego
def wiecej_niz(napis, prog):
    litery = {}
    wynik = set()
    for litera in napis:
        litery[litera] = litery.get(litera, 0) +1
        if napis.count(litera)>prog:
            wynik.add(litera)
    print(wynik)
wiecej_niz('sadasdadasdaffdfdf', 3)

#Opcja jeszcze bardziej krotka
def wiecej_niz(napis, prog):
    return {znak for znak in napis if napis.count(znak) > prog}

