# Solicitar el año al usuario
anio = int(input("Introduce un año: "))

# Determinar si es bisiesto o no
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
