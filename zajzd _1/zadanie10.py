a=int(input("Podaj liczbę a: "))
b=int(input("Podaj liczbę b: "))
c=input("Wybierz rodzaj operacji (+, -, *, /, **): ")

if b == 0:
    print("nie dziel przez zero cholero")
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="**":
    print(a**b)
else:
    print("Wybrałeś jakieś dziwne rzeczy, czytaj uważnie")
    raise ValueError("Zła wartość")