capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for pais, capital in list(zip(paises, capitales)):
    print(f"La capital de {pais} es {capital}")

marcas = ['adidas', 'rebook', 'fila']
productos = ['tenis', 'gorras', 'chaquetas']
mi_zip = zip(marcas, productos)

espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']
numeros = list(zip(espanol, portugues, ingles))
