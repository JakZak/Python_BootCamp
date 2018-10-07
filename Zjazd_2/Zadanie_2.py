lista = []

while len(lista) <= 10:
    print("Wprowadź do 10 liczb/cyfr w celu obliczenia ich sumy i zapisnia w liście: ")
    a = lista.append(input())
    print(a)
    print(lista)
    print(type(lista))
    if a == "k":
        break
    if len(lista) == 10:
        print("Osiągnąłeś maksymalną ilość wprowadzonych wartośći")
        break
b = sum(lista) / len(lista)
print(b)







