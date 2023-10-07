# Solicitar al usuario que ingrese un texto
texto = input("Ingresa un texto: ")

# Dividir el texto en palabras utilizando el espacio como separador
palabras = texto.split()

# Contar la cantidad de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"La cantidad de palabras en el texto es: {cantidad_palabras}")

