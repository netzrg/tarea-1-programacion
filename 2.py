# Solicitar los dos números enteros al usuario
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

# Determinar cuál es el mayor
if numero1 > numero2:
    mayor = numero1
elif numero2 > numero1:
    mayor = numero2
else:
    mayor = "Ambos números son iguales"

# Mostrar el resultado
print(f"El número mayor es: {mayor}")
