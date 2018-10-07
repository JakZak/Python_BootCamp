lista = []
for i in range(0, 101):
    lista.append(i)
print(lista)

podzielna_przez_3 = []
podzielna_przez_5 = []
wspolne = []

for a in lista:
    if a%3==0:
        print(a)
        podzielna_przez_3.append(a)
print("podzielna przez 3: ", len(podzielna_przez_3))

for b in lista:
    if b%5==0:
        print(b)
        podzielna_przez_5.append(b)
print("podzielna przez 5: ", len(podzielna_przez_5))

for c in lista:
    if c%3==0 or c%5==0:
        print(c)
        wspolne.append(c)

przez_3 = len(podzielna_przez_3)
przez_5 = len(podzielna_przez_5)
wspolne = len(wspolne)

suma = przez_3 + przez_5

print(f"W przedziale od 0-100 jest {suma} liczb podzielnych przez 3 i 5")
print(f"W przedziale od 0-100 jest {wspolne} liczb podzielnych przez 3 lub 5")