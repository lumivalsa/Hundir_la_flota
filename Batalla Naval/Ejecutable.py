import pandas as pd 
import numpy as np
import matplotlib as plt
from IPython.display import display, Image
from Clases import Tablero
import winner
from winner import ganador
import os
import time


def comenzar_juego():
    jug1 = Tablero()
    jug1Impactos = Tablero()
    jug2 = Tablero()
    jug2Impactos = Tablero()

    jug1.init_tablero_aleatorio()
    type(jug1.init_tablero_aleatorio)
    jug2.init_tablero_aleatorio()

    print("Tablero inicial del jugador 1")
    print(pd.DataFrame(jug1.tablero))
    print("\nTablero de impactos del jugador 1")
    print(pd.DataFrame(jug1Impactos.tablero))
    aciertos_jug1 = 0
    aciertos_jug2 = 0
    turno_jugador = 1
    fin = False

    try:
        while (aciertos_jug1 < 10 and aciertos_jug2 < 10) and not fin:
            while turno_jugador == 1:
                x = int(input("Introduce horizontal X entre 0 y 9: "))
                y = int(input("Introduce vertical Y entre 0 y 9: "))

                if x > 9 or y > 9:
                    print("\nError: Cordenadas no validas. Intenta de nuevo.")
                    print("(Para terminar introduce una letra.)")
                    
                    break
                elif jug1Impactos.tablero[x, y] == "X" or jug1Impactos.tablero[x, y] == "A":
                    print("\nPosicion ya tomada. Meter nuevas coordenadas.\n")
                   
                    break
                elif jug2.tablero[x, y] == "O":
                    jug1Impactos.tablero[x, y] = "X"
                    aciertos_jug1 += 1
                    print("\n¡Le has dado!")
                    print("Aciertos Jugador 1:", aciertos_jug1, "\n")
                    print("Mi Tablero principal\n")
                    print(pd.DataFrame(jug1.tablero), "\n")
                    print("Mi Tablero de impactos\n")
                    print(pd.DataFrame(jug1Impactos.tablero), "\n")

                    if aciertos_jug1 == 2:
                        fin = True
                        
                        print("Ganó el jugador 1")
                        winner.ganador()
                        
                        
                        break

                elif jug2.tablero[x, y] == " ":
                    jug1Impactos.tablero[x, y] = "A"
                    turno_jugador = 2
                    print("\n¡Agua!")
                    print("Aciertos Jugador 1:", aciertos_jug1, "\n")
                    print("Mi Tablero principal\n")
                    print(pd.DataFrame(jug1.tablero), "\n")
                    print("Mi Tablero de impactos\n")
                    print(pd.DataFrame(jug1Impactos.tablero), "\n")

            while turno_jugador == 2 and not fin:

                x = np.random.randint(10)
                y = np.random.randint(10)

                if jug2Impactos.tablero[x, y] == "X" or jug2Impactos.tablero[x, y] == "A":
                    break

                elif jug1.tablero[x, y] == "O":
                    jug1.tablero[x, y] = "X"
                    jug2Impactos.tablero[x, y] = "X"
                    aciertos_jug2 += 1
                    print("\n¡Barco alcanzado!")
                    print("Aciertos Jugador 2:", aciertos_jug2, "\n")
                    print("Mi Tablero principal\n")
                    print(pd.DataFrame(jug1.tablero), "\n")

                    if aciertos_jug2 == 3:
                        fin = True
                        
                        print("Ganó el jugador 2")
                       

                elif jug1.tablero[x, y] == " ":
                    jug1.tablero[x, y] = "A"
                    jug2Impactos.tablero[x, y] = "A"
                    turno_jugador = 1
                    print("\n¡Agua!")
                    print("Aciertos Jugador 2:", aciertos_jug2, "\n")
                    print("Mi Tablero principal\n")
                    print(pd.DataFrame(jug1.tablero), "\n")


    except ValueError:
        print("\nJuego terminado.")