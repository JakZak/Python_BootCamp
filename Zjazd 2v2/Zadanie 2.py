nawias1 = 0
nawias2 = 0

my_text = input("Podaj text: ")

for indext in i enumerate(my_text):
    if i=="<":
        nawias1 = index
    if i == ">":
        nawias2 = index
    print(nawias2 - nawias1-1)


#Sposób 2
czy_miedzy_nawiasami = False
licznik = 0
for znak in my_text:
    if znak == "<":
        czy_miedzy_nawiasami = True
    elif znak = ">":
        czy_miedzy_nawiasami = False
    elif czy_miedzy_nawiasami:#w ten sposób nie zlicza pierwszego otwartego nawiasu (elif zamiast nowego if)
        licznik +=1
print (licznik)


