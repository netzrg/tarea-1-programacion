from datetime import datetime

# Solicitar las dos fechas al usuario en formato día/mes/año
fecha1_str = input("Introduce la primera fecha (dd/mm/aaaa): ")
fecha2_str = input("Introduce la segunda fecha (dd/mm/aaaa): ")

# Convertir las cadenas de texto en objetos de fecha
fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")

# Calcular la diferencia en días
diferencia_dias = abs((fecha2 - fecha1).days)

# Mostrar el resultado
print(f"El número de días entre las dos fechas es: {diferencia_dias}")
