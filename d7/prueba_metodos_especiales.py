class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


print(Libro('It', 'Stephen King', 710))


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas=710):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)


print(len(Libro('It', 'Stephen King')))


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")


libro_terror = Libro('It', 'Stephen King', 710)

del libro_terror  # Borra la instancia
