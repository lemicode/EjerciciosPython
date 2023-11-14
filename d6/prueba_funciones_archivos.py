def abrir_leer(archivo):
    fichero = open(archivo)
    texto = fichero.read()
    fichero.close()
    return texto


def sobrescribir(archivo):
    texto = open(archivo, 'w')
    texto.write("contenido eliminado")
    texto.close


def registro_error(archivo):
    fichero = open(archivo, 'a')
    fichero.write("se ha registrado un error de ejecución")
    fichero.close()
