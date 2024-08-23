# Solicitar los valores de a y b al usuario
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))

# Calcular el valor de x en la ecuación ax + b = 0
if a != 0:
    x = -b / a
    print(f"El valor de x es: {x}")
else:
    print("La ecuación no tiene solución (a no puede ser cero).")
