import bs4
import requests

# Previamente se instaló lxml: pip install lxml

# Creación de una url sin número de página
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar páginas
for pagina in range(1, 51):

    # Crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Selecionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:

        # Chequear que tenga 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver libro 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
