nombre = input("Ingresa tu nombre: ")
ventas = input("Ingresa el total de ventas del mes: ")
comision = round(((int(ventas) * 13) / 100), 2)
print(f"{nombre}, tu comisión es de ${comision}")