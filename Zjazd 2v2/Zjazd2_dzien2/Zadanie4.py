x = 'koszt $cena PLN,' \
    'kwota $cena brutto'


# def formatowanie_tekstu(cena, *args):
#     for text in args:
#         text = text.replace("$cena", str(cena))
#
#     return text

# def formatowanie_tekstu(cena, *args):
#     out = []
#     for text in args:
#         text = text.replace("$cena", str(cena))
#         out.append(text)
#     return '\n'.join(out)


# print(formatowanie_tekstu(10, x))

#rozwiazanie prowadzacego

# def formatuj(cena, *args):
#     out = []
#     for text in args:
#         text = text.replace('$cena', cena)
#         out.append(text)
#         return "\n".join(out)

#inny miodel
# def formatuj(*args, **kwargs):
#     out = []
#     for text in args:
#         for k in kwargs:
#             text = text.replace(f'${k}', str(kwargs[k]))
#             out.append(text)
#         return "\n".join(out)

# print(formatuj(x, cena = 10))

#Testy
def formatuj(*args, **kwargs):
    po_formacie = []
    for text in args:
        for k in kwargs:
            text = text.replace(f'${k}', str(kwargs[k]))
            po_formacie.append(text)
        return "\n".join(po_formacie)

print(formatuj (x, cena=10))