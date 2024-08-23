# Solicitar los valores necesarios al usuario
capital = float(input("Introduce el capital inicial: "))
tasa = float(input("Introduce la tasa de interés anual (en porcentaje): ")) / 100
anos = float(input("Introduce el número de años: "))

# Calcular el interés y el monto total
interes = capital * tasa * anos
monto_total = capital + interes

# Mostrar los resultados
print(f"El interés simple es: {interes}")
print(f"El monto total acumulado es: {monto_total}")
