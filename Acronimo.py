#Solicitar al usuario que ingrese una frase 
frase = input("Ingresa una frase  para generar un acronimo:")

##Dividir la frase en palabras
palabras = frase.split()

# Inicializar una variable para el acrónimo
acronimo = ""

# Obtener la inicial de cada palabra y agregarla al acrónimo en mayúsculas
for palabra in palabras:
    acronimo += palabra[0].upper()

# Mostrar el acrónimo
print(f"Acrónimo: {acronimo}")