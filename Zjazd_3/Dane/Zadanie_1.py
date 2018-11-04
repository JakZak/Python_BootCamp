# with open("text.txt", 'w') as f:
#     f.write("pierwsza linia pliku\ndruga linia pliku")
#
# with open ("text.txt") as f:
#     f.read()
#
# with open("text.txt") as f:
#     for line in f:


# import sys
#
# if len(sys.argv) > 1:
#     nazwa_pliku = sys.argv[1]
#
#     with open(nazwa_pliku) as f:
#         for line in f:
#             print(line, end = "")
# else:
#     print("podaj nazwę pliku")


import sys

if len(sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:
        for i, line in enumerate(f, start=1):
            print(i, line, end="")
else:
    print("podaj nazwę pliku")

