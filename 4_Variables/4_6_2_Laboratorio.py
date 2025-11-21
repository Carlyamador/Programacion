# Ejercicio float: Suma de litros purificados en AquaPure

# Mensaje de bienvenida
print("Bienvenido al sistema de AquaPure")
print("Vamos a calcular la cantidad total de litros purificados.\n")

# Pedimos al usuario la cantidad de litros purificados en el tanque A
litros_tanque_A_input = input("Ingrese los litros purificados en el tanque A: ")
# Convertimos el valor ingresado a decimal (float)
litros_tanque_A = float(litros_tanque_A_input)
print("Litros tanque A:", litros_tanque_A)

# Pedimos al usuario la cantidad de litros purificados en el tanque B
litros_tanque_B_input = input("Ingrese los litros purificados en el tanque B: ")
# Convertimos el valor ingresado a decimal (float)
litros_tanque_B = float(litros_tanque_B_input)
print("Litros tanque B:", litros_tanque_B)

# Calculamos el total de litros purificados sumando ambos tanques
total_litros = litros_tanque_A + litros_tanque_B

# Mostramos el resultado paso a paso
print("\nCalculando la producción total de litros purificados...")
print("Suma tanque A + tanque B = {} + {}".format(litros_tanque_A, litros_tanque_B))
print("El total de litros purificados es:", total_litros)
