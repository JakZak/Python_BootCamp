napis = input("Podaj napis: ")
SAMOGLOSKA = "aeiou"
liczba_samoglosek = 0

for znak in napis:
    if znak in SAMOGLOSKA:
        liczba_samoglosek +=1
print(liczba_samoglosek)

