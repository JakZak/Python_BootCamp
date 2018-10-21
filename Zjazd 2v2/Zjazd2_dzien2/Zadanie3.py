
def policz_litery (napis, start = '<', stop = '>'):
    zaglebienie = 0
    wynik = 0
    for znak in napis:
        if znak == start :
            zaglebienie += 1
        elif znak == stop:
            zaglebienie -= 1
        else:
            wynik += zaglebienie
    return wynik




def test_liczenie_liczby_znakow_bez():
    assert policz_litery('napis') == 0

def test_liczenie_liczby_znakow_puste():
    assert policz_litery('') == 0

def test_liczenie_liczby_znakow_1():
    assert policz_litery('ala ma <kota> a kot ma ale') == 4

def test_liczenie_liczby_znakow_2():
    assert policz_litery ('ala [kota [a kot]] ma [ale]', '[', ']') == 18

def test_liczeie_liczby_znakow_3 ():
    assert policz_litery ('a <a<a<a>>>') == 6

