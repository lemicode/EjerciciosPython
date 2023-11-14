valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [v**2 for v in valores]

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [v for v in valores if v % 2 == 0]

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(t - 32) * (5/9) for t in temperatura_fahrenheit]
