
print("Bienvenido, por favor, selecciona una canción de este top de 5 canciones:")
#Se añaden opciones de canciones para la cual el usuario eligira una y se le proporcionara la letra
canciones = {
    "Last Surprise by  Persona5 Royal": "You'll never see it coming You'll see that my mind is too fast for eyes You're done in By the time it's hit you, your last surprise",
    "Entregate Luis Miguel": "Déjame robar El gran secreto de tu piel Déjate llevar Por tus instintos de mujer Entrégate Aún no te siento Deja que tu cuerpoSe acostumbre a mi calor",
    "Crawling Linkin Park": " Crawling in my skin These wounds, they will not heal Fear is how I fall Confusing what is real",
   "Padoru Padoru": " Hashire sori yo Kaze no you ni Tsukimihara wo Padoru Padoru Padoru Padoru Pado Padoru Padoru Padoru Pado Padoru",
    "Rosa Pastel by Belanova": " No, no quiero ser esa mujer Ella se fue a un abismo Tú no eres aquel que prometió Sería mi superhéroe y que Todo acabó No queda más Seremos dos extraños",
}



for i, cancion in enumerate(canciones, start=1):
    print(f"{i}. {cancion}")

seleccion = int(input())
if 1 <= seleccion <= len(canciones):
    cancion_seleccionada = list(canciones.keys())[seleccion - 1]
    letra = canciones[cancion_seleccionada]
    print(f"Has seleccionado '{cancion_seleccionada}'. Te mostramos la letra a continuación:\n")
    print("-------", cancion_seleccionada, "------------")
    print(letra)
else:
    print("Selección no válida.")