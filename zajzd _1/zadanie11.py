print("Proszę o podanie wymiarów planszy na której znajdować się będą postacie")
x = int(input("Szerokość planszy jako liczba całkowita: "))
y = int(input("Długość planszy jako liczba całkowita: "))

print("Jeśli chcesz dowiedzieć się gdzie znajduje się twoja postać na planszy, "
      "podaj jej współrzędne a-szerokość, b-długość")
a=int(input("a: "))
b=int(input("b: "))

if a>x or b>y:
    print("O stary chyba troche wyleciałeś z planszy xD!!!")

procent_10x = x*0.1
print(procent_10x)
procent_10y = y*0.1
print(procent_10y)

procent_90x = x*0.9
print(procent_90x)
procent_90y = y*0.9
print(procent_90y)

if a>procent_10x and a<procent_90x:
    if b<procent_10y:
        print("Znajdujesz sięw dolnej granicy planszy")
    elif b>procent_90y:
        print("Znajdujesz się w górnej granicy mapy")
elif a<procent_10x:
    if b>procent_10y and b<procent_90y:
        print("Znajdujesz się w lewej części mapy")
elif a>procent_90x:
    if b>procent_10y and b<procent_90y:
        print("Znajdujesz się w prawej części mapy")
elif a<procent_10x and b<procent_10y:
    print("Znajdujesz sięw lewym dolnym rogu")
elif a > procent_90x and b < procent_10y:
    print("Znajdujesz sięw prawym dolnym rogu")
elif a<procent_10x and b>procent_90y:
    print("Znajdujesz sięw lewym górnym rogu")
elif a>procent_90x and b>procent_90y:
    print("Znajdujesz się w prawym górnym rogu")
else:
    print("Jesteś w centrum mapy, UWAŻĄJ!")





