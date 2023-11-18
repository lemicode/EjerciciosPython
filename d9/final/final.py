"""
    Se sugiere emplear el siguiente comando para la ejecución del código, y con ello mejorar la lectura:

    python3 final.py | less
"""

import os
import re
import datetime
import math
import time
from pathlib import Path
import textwrap


def buscar_codigos():
    ruta = 'Mi_Gran_Directorio'
    patron = r'N[A-Z,a-z]{3}-\d{5}'
    fecha_busqueda = datetime.date.today().strftime('%d/%m/%y')

    for carpeta, subcarpetas, archivos in os.walk(ruta):
        inicio = time.time()
        lista_archivos = []

        for archivo in archivos:
            texto_archivo = Path(carpeta, archivo).read_text()
            busqueda_patron = re.search(patron, texto_archivo)

            if busqueda_patron:
                lista_archivos.append((archivo, busqueda_patron.group()))

        cantidad_hallazgos = len(lista_archivos)

        if cantidad_hallazgos > 0:
            print(textwrap.dedent(f"""
                {'-' * 52}
                Fecha de búsqueda: {fecha_busqueda}
                Ruta: {carpeta}
            """))
            print('ARCHIVO\t\t\tNRO. SERIE\n-------\t\t\t----------')

            for nombre_archivo, cod_serie in lista_archivos:
                print(f'{nombre_archivo}\t\t{cod_serie}')

            print(f'\nCantidad de archivos con hallazgo: {cantidad_hallazgos}')
            final = time.time()
            duracion = math.ceil(final - inicio)
            print(f'Duración de la búsqueda: {duracion} segundos')
            print('-' * 52)


buscar_codigos()
