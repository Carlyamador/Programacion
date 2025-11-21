# Ejercicio int: Suma de paquetes procesados en LogiExpress

# Mensaje inicial
print("Bienvenido al sistema de LogiExpress")
print("Vamos a calcular el total de paquetes procesados en la jornada.\n")

# Pedimos al usuario la cantidad de paquetes enviados en la mañana
paquetes_manana_input = input("Ingrese la cantidad de paquetes enviados en la mañana: ")
paquetes_manana = int(paquetes_manana_input)
print("Paquetes mañana:", paquetes_manana)

# Pedimos al usuario la cantidad de paquetes enviados en la tarde
paquetes_tarde_input = input("Ingrese la cantidad de paquetes enviados en la tarde: ")
paquetes_tarde = int(paquetes_tarde_input)
print("Paquetes tarde:", paquetes_tarde)

# Pedimos al usuario la cantidad de paquetes enviados en la noche
paquetes_noche_input = input("Ingrese la cantidad de paquetes enviados en la noche: ")
paquetes_noche = int(paquetes_noche_input)
print("Paquetes noche:", paquetes_noche)

# Sumamos los paquetes de todos los turnos
total_paquetes = paquetes_manana + paquetes_tarde + paquetes_noche

# Mostramos el resultado paso a paso
print("\nCalculando el total de paquetes procesados...")
print("Suma mañana + tarde + noche = {} + {} + {} ".format(paquetes_manana, paquetes_tarde, paquetes_noche))
print("El total de paquetes procesados en la jornada es:", total_paquetes)

