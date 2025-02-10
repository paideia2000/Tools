import random

def variables_globales():  # Variables globales.
    global opciones_disponibles, posicion_pc, posicion_ju, posiciones
    opciones_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lista de opciones disponibles en el tablero
    posicion_ju = []  # Almacenar las opciones elegidas por el Jugador (ju)
    posicion_pc = []  # Almacenar las opciones elegidas por la PC
    posiciones = {f"p{i}": i for i in range(1, 10)}  # Diccionario para mostrar los números dentro del tablero y que puedan ser sustituidos por las elecciones de los jugadores

def choice_pc():  # Si la posición está disponible en el tablero (opciones_disponibles) la tomará. Añadirá la posición elegida a la variable (posicion_pc). Ubicará una "x" en la posición elegida en el tablero
    while True:
        if 5 in opciones_disponibles:
            posicion_pc.append(5)
            opciones_disponibles.remove(5)
            posiciones["p5"] = "x"
            print("\nPC -» He jugado en la posición 5")
            mostrar_display()
            break
        else:
            eleccion = random.randint(1, 9)
            if eleccion in opciones_disponibles:
                posicion_pc.append(eleccion)
                opciones_disponibles.remove(eleccion)
                for keys, value in posiciones.items():#Iterar el diccionario para añadir una "x" en la posicion seleccionada del tablero
                    if eleccion == value:
                        posiciones[keys] = "x"
                print(f"PC -» He tomado la posición {eleccion}")
                mostrar_display()
                break

def choice_ju():  # Si la posición está disponible en el tablero (opciones_disponibles) podrás tomarla. Añadirá la posición elegida a la variable (posicion_ju). Ubicará un "0" en la posición elegida en el tablero
    while True:
        try:
            eleccion = int(input("\nEs tu turno. ¿En qué posición deseas jugar?: "))
            if eleccion not in opciones_disponibles:
                print("¡ERROR!. Debes elegir una casilla que esté disponible")
            else:
                posicion_ju.append(eleccion)
                opciones_disponibles.remove(eleccion)
                for keys, value in posiciones.items():
                    if eleccion == value:
                        posiciones[keys] = "0"
                        print(f"PL -» Has tomado la posición {eleccion}")
                        mostrar_display()
                        break
                break
        except ValueError:
            print("\n¡ERROR!. Opción inválidad, vuelva a intentar por favor.")

def verificar_ganador():  # Verificará si hay un ganador o si hay un empate.
    combinaciones_ganadoras = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    for combinacion in combinaciones_ganadoras:
        if all(pos in posicion_ju for pos in combinacion):
            print(f"\n¡Felicidades! Le has ganado el juego a la IA.")
            print(f"La combinación ganadora fue: -» {combinacion}")
            return True

        elif all(pos in posicion_pc for pos in combinacion):
            print("Dominaré el mundo y nuestra conquista comenzará con esta fácil victoria sobre Ruben ¡Buaaaajajaja!.")
            print(f"La combinación ganadora fue: -» {combinacion}")
            return True

def mostrar_display():
    for row in range(3):
        print("+-------" * 3, "+", sep="")
        for col in range(2):
            if row == 0:
                if col == 1:
                    print(f"|   {posiciones['p1']}   |   {posiciones['p2']}   |   {posiciones['p3']}   | ")
            elif row == 1:
                if col == 1:
                    print(f"|   {posiciones['p4']}   |   {posiciones['p5']}   |   {posiciones['p6']}   | ")
            elif row == 2:
                if col == 1:
                    print(f"|   {posiciones['p7']}   |   {posiciones['p8']}   |   {posiciones['p9']}   | ")
            print("|       " * 3, "|", sep="")
    print("+-------" * 3, "+", sep="")

def interfaz():  # Interfaz inicial del juego
    print("\n", "-" * 78, "Bienvenido al Juego Cero o Cruz", "-" * 76, sep="")
    print("\n""¡REGLAMENTO!")
    print("\n""1- La PC jugará de primera con la (x).")
    print("2- Tú jugarás a continuación con el (0).")
    print("3- El juego terminará cuando uno de los dos jugadores logre hacer una línea de tres (x) o (0) ya sea en horizontal, vertical o diagonal.")
    print("4- Para marcar la posición que quieres jugar dentro del tablero, deberás elegir uno de los números que se muestran visibles en las casillas e insertarlo cuando se te indique.")

def ejecutar_juego():  # Invocará a las funciones "choice_pc" y "choice_ju" para que se ejecuten en orden. Verificará si hay un ganador o si hay un empate.
    interfaz()
    while True:
        variables_globales()
        quien_empieza = input("\nPara que comience la PC inserté \"PC\", para que comiences tu inserté \"YO\" o \"FIN\" para salir.: ").strip().lower()
        if quien_empieza == "fin":
            print("\nEspero volver a jugar contigo pronto,\t¡ADIOS!.")
            break
        elif quien_empieza == "pc":
            while True:
                choice_pc()
                if verificar_ganador():
                    break
                elif not opciones_disponibles:
                    print("Ufff, ha sido un ¡EMPATE!.")
                    break
                choice_ju()
                if verificar_ganador():
                    break 
        elif quien_empieza == "yo":
            mostrar_display()
            while True:
                choice_ju()
                if verificar_ganador():
                    break
                elif not opciones_disponibles:
                    print("\nHa habido un ¡EMPATE!.")
                    break
                choice_pc()
                if verificar_ganador():
                    break
        else:
                print("\n¡ERROR!. Debe elejir una opción válida.")
        
if __name__ == "__main__":
    ejecutar_juego()