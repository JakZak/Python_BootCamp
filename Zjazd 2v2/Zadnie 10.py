napis = input("Podaj swój napis:\n")
znaki = []
for z in napis:
    znaki += [z]
print(znaki)

licznik_liter = {}

# for litera in napis:
#     if litera in licznik_liter:
#         licznik_liter[litera] += 1
#     elif litera not in licznik_liter:
#         if litera == " ":
#             pass
#         else:
#             licznik_liter[litera] = 1
#
# for z in licznik_liter:
#     print(f"W twoim napisie '{napis}', znak: [{z}] wystąpił \n{licznik_liter[z]} razy")


#Wykonanie przez prowadzącego

for litera in licznik_liter:
    licznik_liter[litera] = licznik_liter.get(litera, 0) +1
print(f"W twoim napisie '{napis}', znak: [{litera}] wystąpił \n{licznik_liter[litera]} razy")