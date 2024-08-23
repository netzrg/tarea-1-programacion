# Solicitar el monto de la compra y la tasa de impuesto al usuario
monto = float(input("Introduce el monto de la compra: "))
tasa = float(input("Introduce la tasa de impuesto (en porcentaje): "))

# Calcular el impuesto y el total a pagar
impuesto = monto * tasa / 100
total_pagar = monto + impuesto

# Mostrar los resultados
print(f"El impuesto a pagar es: {impuesto}")
print(f"El total a pagar es: {total_pagar}")
