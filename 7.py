# Solicitar el ancho y la altura del rectángulo al usuario
ancho = float(input("Introduce el ancho del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# Calcular el perímetro y el área del rectángulo
perimetro = 2 * (ancho + altura)
area = ancho * altura

# Mostrar los resultados
print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")
