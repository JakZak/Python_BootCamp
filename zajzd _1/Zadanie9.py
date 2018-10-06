rok_urodzenia = int(input("Podaj swój rok urodzenia: "))
import datetime
czas=datetime.datetime.now()

wiek=czas.year-rok_urodzenia

if  wiek>=18:
    print("Możesz wejść, jesteś pełnoletni")
else:
    print("Do mleka małolacie")


