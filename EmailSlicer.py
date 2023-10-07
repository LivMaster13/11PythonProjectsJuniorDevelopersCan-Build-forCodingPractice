# Solicitar al usuario que ingrese su dirección de correo electrónico
email = input("Ingresa tu dirección de correo electrónico: ")

# Dividir la dirección de correo electrónico en nombre de usuario y dominio
usuario, dominio = email.split("@")

# Mostrar el nombre de usuario y el dominio por separado
print(f"Tu Nombre de usuario es : {usuario}")
print(f"El servidor de Dominio es: {dominio}")

