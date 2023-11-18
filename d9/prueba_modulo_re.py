"""
Algunos cuantificadores y caracteres especiales para
formar patrones

[] un set de caracteres
. un caracter cualquiera
^ inicia con
$ finaliza con
* cero o más concurrencias
+ una o más concurrencias
{} un número especificado de ocurrencias. Ejemplo: {n}, {n, m}, {n,}
? cero o una ocurrencia
| operador lógico 'O'

\d dígito numérico
\D NO numérico
\w caracter alfanumérico
\W NO alfanumérico
\s especio en blanco
\S NO espacio en blanco

Ejemplo módulo re:
patro = r'' # Esta es la forma en el caso que contenga caracteres especiales
              o cuantificadores de lo contrario solo se dejaría el string, así 'texto'.
re.search(patron, "algo123")

Funciones:
search(): devuelve un objeto 'match' con el primer hallazgo
findall(): devuelve una lista con todos los hallazgos
finditer(): devuelve una lista de objetos tipo 'search'
"""

import re


def verificar_email(email):
    patron = r'^\w+@\w+\.[a-z,A-Z]{2,3}(.[a-z,A-Z]{2})?$'
    if re.search(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


def verificar_saludo(frase):
    if re.search('Hola', frase):
        print("Ok")
    else:
        print("No has saludado")


def verificar_cp(cp):
    patron = r'^[A-Z,a-z]{2}\d{4}$'
    if re.search(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
