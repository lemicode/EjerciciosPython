import bs4
import requests

# Previamente se instaló lxml: pip install lxml

resultado = requests.get('https://github.com/bamboothink')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('img.avatar')[0]['src']

imagen_1 = requests.get(imagenes)

archivo = open('avatar.jpg', 'wb')
archivo.write(imagen_1.content)
archivo.close()
