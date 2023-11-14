import os
from pathlib import Path
import subprocess


def abrir_programa_recetas():
    try:
        ruta_recetas = Path('Recetas')
        ruta_completa = Path(Path.home(), ruta_recetas)
        crear_recetario(ruta_recetas)
        print('\n' + "*" * 30)
        print('¡Bienvenido a este recetario!')
        print("*" * 30 + '\n')
        print(f'La ruta a la carpeta de recetas es: {ruta_completa}')
        mostrar_menu_principal(ruta_recetas)
    # except Exception as e:
    #     print(f'\nSe ha producido una excepción: {e}\n')
    except ValueError as f:
        print(f'\nDebe ingresar un número de opción válido.\n\n')
    except IndexError as c:
        print(f'\nDebe ingresar un número de opción dentro del rango del menú.\n\n')


def crear_recetario(ruta_recetas):
    if not ruta_recetas.exists():
        os.mkdir('Recetas')
        os.mkdir('Recetas/Carnes')
        os.mkdir('Recetas/Ensaladas')
        os.mkdir('Recetas/Pastas')
        os.mkdir('Recetas/Postres')
        filePath = Path(ruta_recetas, 'Carnes', 'Etrecot al Malbec.txt')
        filePath.write_text('Ejemplo Etrecot al Malbec')
        filePath = Path(filePath.parent, 'Matambre a la Pizza.txt')
        filePath.write_text('Ejemplo Matambre a la Pizza')
        filePath = Path(filePath.parent.parent, 'Ensaladas', 'Ensalada Griega.txt')
        filePath.write_text('Ejemplo Ensalada Griega')
        filePath = Path(filePath.parent, 'Ensalada Mediterranea.txt')
        filePath.write_text('Ejemplo Ensalada Mediterranea')
        filePath = Path(filePath.parent.parent, 'Pastas', 'Canelones de Espinaca.txt')
        filePath.write_text('Ejemplo Canelones de Espinaca')
        filePath = Path(filePath.parent, 'Ravioles de Rocotta.txt')
        filePath.write_text('Ejemplo Ravioles de Rocotta')
        filePath = Path(filePath.parent.parent, 'Postres', 'Compota de Manzana.txt')
        filePath.write_text('Ejemplo Compota de Manzana')
        filePath = Path(filePath.parent, 'Tarta de Frambuesa.txt')
        filePath.write_text('Ejemplo Tarta de Frambuesa')


def leer_recetas(ruta_recetas, categorias):
    numero_categoria = mostrar_categorias(categorias)
    recetas_categoria = obtener_recetas_por_categoria(ruta_recetas, categorias, numero_categoria)
    if len(recetas_categoria) == 0:
        print('\nLa categoría seleccionada no contiene recetas\n')
    else:
        numero_receta = mostrar_recetas(recetas_categoria)
        receta_seleccionada = recetas_categoria[int(numero_receta) - 1]
        print('\n' + '*' * 30)
        print(f'Receta {receta_seleccionada.stem}:\n')
        print(receta_seleccionada.read_text())
        print('*' * 30 + '\n')


def crear_receta(ruta_recetas, categorias):
    numero_categoria = mostrar_categorias(categorias)
    categoria_seleccionada = categorias[int(numero_categoria) - 1]
    nombre_nueva_receta = input('Ingrese el nombre de la receta: ')
    contenido_nueva_receta = input('Ingrese el contenido de la nueva receta: ')
    ruta_nueva_receta = Path(ruta_recetas, categoria_seleccionada, nombre_nueva_receta + '.txt')
    ruta_nueva_receta.write_text(contenido_nueva_receta)
    print(f'\n\nLa nueva receta se ha creado en la ruta "{ruta_nueva_receta}"\n')


def editar_receta(ruta_recetas, categorias):
    numero_categoria = mostrar_categorias(categorias)
    recetas_categoria = obtener_recetas_por_categoria(ruta_recetas, categorias, numero_categoria)
    numero_receta = mostrar_recetas(recetas_categoria)
    ruta_receta_seleccionada = recetas_categoria[int(numero_receta) - 1]
    subprocess.run(['nano', ruta_receta_seleccionada])


def eliminar_receta(ruta_recetas, categorias):
    numero_categoria = mostrar_categorias(categorias)
    recetas_categoria = obtener_recetas_por_categoria(ruta_recetas, categorias, numero_categoria)
    if len(recetas_categoria) != 0:
        numero_receta = mostrar_recetas(recetas_categoria)
        ruta_receta_seleccionada = recetas_categoria[int(numero_receta) - 1]
        ruta_receta_seleccionada.unlink()
        print(f'\nLa receta "{ruta_receta_seleccionada}" fue eliminada!\n')
    else:
        print('\nLa categoría seleccionada no contiene recetas\n')


def crear_categoria(ruta_recetas):
    nombre_nueva_categoria = input('Ingrese el nombre de la nueva categoría: ')
    os.mkdir(Path(ruta_recetas, nombre_nueva_categoria))
    print('\nCategoría creada!\n')


def eliminar_categoria(ruta_recetas, categorias):
    numero_categoria = mostrar_categorias(categorias)
    ruta_categoria_seleccionada = Path(ruta_recetas, categorias[int(numero_categoria) - 1])
    for receta_categoria in Path(ruta_categoria_seleccionada).glob('*.txt'):
        receta_categoria.unlink()
    ruta_categoria_seleccionada.rmdir()
    print('\nCategoría eliminada!\n')


def mostrar_menu_principal(ruta_recetas):
    continuar_programa = True
    while continuar_programa:
        recetas = [receta.name for receta in ruta_recetas.glob('**/*.txt')]
        categorias = [categoria.name for categoria in ruta_recetas.glob('*/**')]
        total_recetas = len(recetas)
        print(f'\nHay en total {total_recetas} recetas.\n')
        print('[1] Leer receta')
        print('[2] Crear receta')
        print('[3] Editar receta')
        print('[4] Eliminar receta')
        print('[5] Crear categoría')
        print('[6] Eliminar categoría')
        print('[7] Finalizar programa')
        opcion = input('\nElige una opción: ')
        print('')
        match opcion:
            case '1':
                leer_recetas(ruta_recetas, categorias)
            case '2':
                crear_receta(ruta_recetas, categorias)
            case '3':
                editar_receta(ruta_recetas, categorias)
            case '4':
                eliminar_receta(ruta_recetas, categorias)
            case '5':
                crear_categoria(ruta_recetas)
            case '6':
                eliminar_categoria(ruta_recetas, categorias)
            case _:
                continuar_programa = False
                print("\nPrograma finalizado!\n\n")


def mostrar_categorias(categorias):
    for indice, categoria in enumerate(categorias):
        print(f'[{indice + 1}] {categoria}')
    numero_categoria = input('\nElige una opción: ')
    print('')
    return numero_categoria


def obtener_recetas_por_categoria(ruta_recetas, categorias, numero_categoria):
    recetas_categoria = []
    for receta_categoria in Path(ruta_recetas, categorias[int(numero_categoria) - 1]).glob('*.txt'):
        recetas_categoria.append(receta_categoria)
    return recetas_categoria


def mostrar_recetas(recetas_categoria):
    for indice, receta in enumerate(recetas_categoria):
        print(f'[{indice + 1}] {receta.stem}')
    numero_receta = input('\nElige una opción: ')
    print('')
    return numero_receta


abrir_programa_recetas()
