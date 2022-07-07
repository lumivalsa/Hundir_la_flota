import numpy as np
import pandas as pd
import matplotlib as plt
from IPython.display import display, Image
from Clases import Tablero
import Ejecutable
import os 
import time 
from tkinter import*



print("Combate Naval")
print("Bienvenido al juego ")
img=tk.PhotoImage(file="combate_naval.png")
lbl_img=tk.Label(ventana, image=img)
lbl_img.pack()

time.sleep(1)
os.system("clear")

print()
print("Estas a punto de vivir una experiencia de juego innovidable, que podrá reemplazar a todos los juegos de tu infacia.")
print()

Ejecutable.comenzar_juego()