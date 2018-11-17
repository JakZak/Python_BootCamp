import json

import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=json") as f:
    print (f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print (f"- {r['code']} - {r['mid']}")

waluta = input ("Wprowadź skrót podanej waluty na którą chcesz dokonać wymiany: ")
kwota = float(input ("Podaj kwotędo wymiany: "))

for r in rates:
    if r['code'] == waluta:
        result = kwota * r['mid']
        print(result)

