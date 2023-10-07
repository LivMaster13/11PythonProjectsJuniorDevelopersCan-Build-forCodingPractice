from random import randint

# Crear una lista de opciones de juego
opciones = ["Piedra", "Papel", "Tijeras"]

# Asignar una opción de juego aleatoria a la computadora
computadora = opciones[randint(0, 2)]

# Inicializar la variable del jugador como Falso
jugador = False

while jugador == False:
    # Establecer la variable del jugador como Verdadero
    jugador = input("Piedra, Papel, Tijeras? ")
    if jugador == computadora:
        print("¡Empate!")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("¡Has perdido:(!", computadora, "cubre", jugador)
        else:
            print("¡Has ganado:D!", jugador, "aplasto", computadora)
    elif jugador == "Papel":
        if computadora == "Tijeras":
            print("¡Has perdido!", computadora, "", jugador)
        else:
            print("¡Has ganado:D!", jugador, "cubre", computadora)
    elif jugador == "Tijeras":
        if computadora == "Piedra":
            print("¡Has perdido:...", computadora, "aplasto", jugador)
        else:
            print("¡Has ganado!", jugador, "corto", computadora)
    else:
        print("Esa no es un valor a ingresar valido. Ingresa unicamente lo solicitado")
    # La variable del jugador se estableció como Verdadero, pero la queremos como Falso para que el bucle continúe
    jugador = False
    computadora = opciones[randint(0, 2)]