# Solicitar los coeficientes de la ecuación cuadrática al usuario
a = float(input("Introduce el coeficiente 'a': "))
b = float(input("Introduce el coeficiente 'b': "))
c = float(input("Introduce el coeficiente 'c': "))

# Calcular el discriminante
discriminante = (b ** 2) - (4 * a * c)

# Mostrar el resultado
print(f"El discriminante de la ecuación es: {discriminante}")
