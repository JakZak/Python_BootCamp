lista = [-1, 100, 20, 30, -15, 0, 200, -8, 44]


ujemne = []
dodatnie = []

for a in lista:
    if a<0:
        ujemne.append(a)

for b in lista:
    if b > 0:
        dodatnie.append(b)

print (len(ujemne))
print (len(dodatnie))

# 2 opcja

lista = [-1, 100, 20, 30, -15, 0, 200, -8, 44]

ujemne = 0
dodatnie = 0

for a in lista:
    if a<0:
        ujemne =+ 1

for b in lista:
    if b > 0:
        dodatnie =+ 1


print (ujemne)
print (dodatnie)
