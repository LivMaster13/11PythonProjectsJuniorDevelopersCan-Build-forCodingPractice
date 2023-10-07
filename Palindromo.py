# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    # Eliminar espacios y convertir la cadena a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Solicitar al usuario que ingrese una palabra o frase
entrada = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

# Verificar si la entrada es un palíndromo
if es_palindromo(entrada):
    print(f"'{entrada}' es un palíndromo.")
else:
    print(f"'{entrada}' no es un palíndromo.")

    