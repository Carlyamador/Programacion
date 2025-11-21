# Ejercicio str: Registro de nombres en CustomerFirst

# Mensaje de bienvenida
print("Bienvenido al sistema de CustomerFirst")
print("Vamos a registrar el nombre del agente y del cliente atendido.\n")

# Pedimos al usuario ingresar el nombre del agente
nombre_agente_input = input("Ingrese el nombre del agente: ")
# Guardamos el valor ingresado en una variable de tipo texto (str)
nombre_agente = str(nombre_agente_input)
print("Nombre del agente registrado:", nombre_agente)

# Pedimos al usuario ingresar el nombre del cliente
nombre_cliente_input = input("Ingrese el nombre del cliente: ")
# Guardamos el valor ingresado en una variable de tipo texto (str)
nombre_cliente = str(nombre_cliente_input)
print("Nombre del cliente registrado:", nombre_cliente)

# Combinamos los textos para mostrar un mensaje final
mensaje_final = "El agente " + nombre_agente + " atendió al cliente " + nombre_cliente
print("\nResultado final:")
print(mensaje_final)
