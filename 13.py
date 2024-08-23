import math

# Solicitar el radio de la esfera al usuario
radio = float(input("Introduce el radio de la esfera: "))

# Calcular el área y el volumen de la esfera
area = 4 * math.pi * (radio ** 2)
volumen = (4/3) * math.pi * (radio ** 3)

# Mostrar los resultados
print(f"El área de la esfera es: {area}")
print(f"El volumen de la esfera es: {volumen}")
