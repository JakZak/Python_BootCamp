from requests import get
from bs4 import BeautifulSoup

url = "https://helion.pl/search?qa=&serwisyall=0&szukaj=python&wprzyg=0&wsprzed=1&wyczerp=#"

respone = get(url)

html_soup = BeautifulSoup(respone.text, "html.parser")

books = html_soup.find_all('div', class_ ="book-info")

print(len(books))