# Solicitar las longitudes de las bases y la altura del trapecio
base1 = float(input("Introduce la longitud de la primera base del trapecio: "))
base2 = float(input("Introduce la longitud de la segunda base del trapecio: "))
altura = float(input("Introduce la altura del trapecio: "))

# Calcular el área del trapecio
area = ((base1 + base2) * altura) / 2

# Mostrar el resultado
print(f"El área del trapecio es: {area}")
