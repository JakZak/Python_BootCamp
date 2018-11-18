import csv

wynik = []

with open ("titanic_train.csv") as csvfile:
    data = csv.reader(csvfile, delimiter = ",")
    dlugosci = set()
    zgon = 0
    zyje = 0
    for row in data:
        if row[1] == "0":
            zgon += 1
        elif row[1] == "1":
            zyje += 1
    procent_zgonow = zgon / zgon + zyje
    procent_zywych = zyje / zgon + zyje
    wynik.append(["Zgony: ", zgon])
    wynik.append(["Przezyli: ", zyje])

with open ("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter = ",")
    dlugosc = {}
    for row in data:
        # print (row['Survived'])
        dlugosc [row['Survived']] = dlugosc.get(row['Survived'], 0) + 1

with open ("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter = ",")
    kobiety = {}
    for row in data:
        if row['Sex'] == 'female':
        # print (row['Survived'])
            kobiety[row['Survived']] = kobiety.get(row['Survived'], 0) + 1
    przezylo = kobiety['1']
    zginelo = kobiety['0']
    result = round(100*przezylo/(przezylo+zginelo), 2)
    wynik.append(["Przezylo z ogolu kobiet:", result])

with open ("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter = ",")
    mezczyzni = {}
    for row in data:
        # print (row['Survived'])
        if row['Sex'] == 'male':
            mezczyzni[row['Survived']] = mezczyzni.get(row['Survived'], 0) + 1
    przezylo = mezczyzni['1']
    zginelo = mezczyzni['0']
    result = round(100 * przezylo / (przezylo + zginelo), 2)
    wynik.append(["Przezylo z ogolu mezczyzn: ", result])

with open ("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter = ",")

    how_many_woman = 0
    sum_woman_age = 0

    how_many_man = 0
    sum_man_age = 0

    unique_age_values = set()

    for row in data:
        unique_age_values.add(row['Age'])
        if row['Age'] != "":
            if row['Sex'] == 'female':
                how_many_woman += 1
                sum_woman_age += float(row["Age"])
            else:
                how_many_man += 1
                sum_man_age += float(row["Age"])
    wynik.append(["średnia wieku kobiet: ", sum_woman_age/how_many_woman])
    wynik.append(["średnia wieku mezczyzn: ", sum_man_age/how_many_man])

import matplotlib.pyplot as plt

dane = [zgon, zyje, how_many_woman, how_many_man]

index = ["Zginęło", "Żyje", "Zginęło\nkobiet", "Zginęło\nmężczyzn"]

colors = ["r", "g", "b", "y"]

plt.bar(index, dane, color = colors)

plt.show()
