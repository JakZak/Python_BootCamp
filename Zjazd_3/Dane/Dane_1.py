file = open("")

with open("") as f:#f moze byc dowolnym znakiem
    print(f.read())
    f.write#nadpisz tresc w pliku

for line in f:
    print(line.upper())

