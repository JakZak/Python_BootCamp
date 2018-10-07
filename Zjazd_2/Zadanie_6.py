liczby = [5, 2, 1, 4, 3]

min_i = None
max_i = None

indeksy = list(range(len(liczby)))

for i in indeksy:
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
        print("min", min_i)
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i
        print("max", max_i)

temp = liczby[min_i]
liczby[min_i] = liczby[max_i]
liczby[0] = temp
print(liczby)

#sposób drugi

liczby[min_i], liczby[max_i] = liczby[max_i], liczby[min_i]
print(liczby)


