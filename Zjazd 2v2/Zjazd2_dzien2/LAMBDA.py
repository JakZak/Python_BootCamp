def podzielna_przez_2(x):
    return x % 2 == 0


print(podzielna_przez_2(12))
print(podzielna_przez_2(11))


# y = lambda x: x%2 == 0
#
# print(y(2))
# print(y(5))

def wybierz(dane, warunek):
    #:param dane - lista liczb
    #: param warunek: jakas funkcja sprawdzajaca
    #:return - przefiltrowana lista
    out = []
    for element in dane:
        if warunek(element):  # czy podzielna przez 2 zgodnie z warunkiem ponizej
            out.append(element)
    return (out)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 122, 123]

print(wybierz(lista, podzielna_przez_2))
print(wybierz(lista, lambda x: x%3==0))

# funkcja podzielna pre z3

def podzielna_przez_3 (x):
    return x%3==0

print(wybierz(lista, podzielna_przez_3))