import math

# Solicitar la longitud de un lado del hexágono al usuario
lado = float(input("Introduce la longitud de un lado del hexágono: "))

# Calcular el área del hexágono regular
area = (3 * math.sqrt(3) / 2) * (lado ** 2)

# Mostrar el resultado
print(f"El área del hexágono regular es: {area}")
