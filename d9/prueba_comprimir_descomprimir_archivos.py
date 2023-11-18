import zipfile
import os
import shutil


# Uso básico de zipfile

carpeta_zip = zipfile.ZipFile('carpeta_comprimida.zip', 'w')
carpeta_zip.write('mi_texto_A.txt')
carpeta_zip.write('mi_texto_B.txt')
carpeta_zip.close()

os.unlink('mi_texto_A.txt')
os.unlink('mi_texto_B.txt')

carpeta_comprimida = zipfile.ZipFile('carpeta_comprimida.zip', 'r')
# extract() sirve para extrar un solo archivo o miembro el cual debe pasarse como parámetro
carpeta_comprimida.extractall()
carpeta_comprimida.close()

# Continuando con el uso básico de shutil

carpeta_origen = '../d1'
archivo_destino = 'carpeta_comprimida2'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('carpeta_comprimida2.zip', 'Carpeta Archivos Extraidos', 'zip')
