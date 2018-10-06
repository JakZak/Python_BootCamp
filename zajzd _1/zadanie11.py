print("Proszę o podanie wymiarów planszy na której znajdować się będą postacie")
x = int(input("Szerokość planszy jako liczba całkowita: "))
y = int(input("Długość planszy jako liczba całkowita: "))

print("Jeśli chcesz dowiedzieć się gdzie znajduje się twoja postać na planszy, "
      "podaj jej współrzędne a-szerokość, b-długość")
a=int(input("a: "))
b=int(input("b: "))

if a>x or b>y:
    print("O stary chyba troche wyleciałeś z planszy xD!!!")

procent_10x = (10*x)/100
procent_10y = (10*y)/100

procent_90x = (90*x)/100
procent_90y = (90*y)/100




