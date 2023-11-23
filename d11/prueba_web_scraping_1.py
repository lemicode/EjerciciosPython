import bs4
import requests

# Previamente se instaló lxml: pip install lxml

resultado = requests.get('http://books.toscrape.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

titulos = sopa.select('.product_pod h3>a')

for titulo in titulos:
    print(titulo.getText())
