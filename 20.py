# Solicitar las longitudes de los tres lados del triángulo al usuario
lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))
lado3 = float(input("Introduce la longitud del tercer lado: "))

# Determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_triangulo = "Isósceles"
else:
    tipo_triangulo = "Escaleno"

# Mostrar el resultado
print(f"El triángulo es: {tipo_triangulo}")

