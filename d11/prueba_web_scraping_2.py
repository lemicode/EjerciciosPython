import bs4
import requests

# Previamente se instaló lxml: pip install lxml

url_base = 'http://books.toscrape.com/'

resultado = requests.get(url_base)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.product_pod img')[0]['src']

# Como la ruta del elemento es relativa fue necesario añadir la url base
imagen_1 = requests.get(url_base + imagenes)

archivo = open('imagen.jpg', 'wb')
archivo.write(imagen_1.content)
archivo.close()
