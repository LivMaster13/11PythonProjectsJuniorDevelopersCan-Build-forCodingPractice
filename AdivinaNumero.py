import random

# Generar un número aleatorio entre 1 y 100 para que adivine el usuario
numero_secreto = random.randint(1, 100)

# Inicializar el contador de intentos y los intentos disponibles
intentos = 0
intentos_disponibles = 3

print("Bienvenido a 'Adivina adivinador el numero'!")
print("Estoy pensando en un número entre 1 y 100.")

while intentos < 3:
    # Solicitar al usuario que adivine el número
    intentos += 1
    intento = int(input(f"Intento {intentos}: Ingresa el numero que crees estoy pensando: "))

    # Comprobar si el intento es correcto
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número:D {numero_secreto} en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor. Te quedan", intentos_disponibles - intentos, "intentos.")
    else:
        print("El número es menor. Te quedan", intentos_disponibles - intentos, "intentos.")

# Si se quedaron sin intentos
if intentos == 3:
    print(f"¡Has perdido! El número secreto era {numero_secreto}.")
    