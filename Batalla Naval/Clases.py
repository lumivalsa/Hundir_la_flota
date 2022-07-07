import numpy as np
import pandas as pd


class Tablero:
    def __init__(self):
        self.tablero = np.full((10, 10), " ")

    def introducir_barco(self, size, nseo, x, y):
   
        for i in range(0, size):
            if nseo == "N":
                self.tablero[x - i, y] = "O"
            if nseo == "S":
                self.tablero[x + i, y] = "O"
            if nseo == "E":
                self.tablero[x, y + i] = "O"
            if nseo == "O":
                self.tablero[x, y - i] = "O"
        
    def full_box(self, size, nseo, x, y):
        full_box = False
        for i in range(0, size):
            if nseo == "N" and ((x - size + 1) < 0 or self.tablero[x - i, y] in ["O"]):
                full_box = True
            if nseo == "S" and ((x + size) > 10 or self.tablero[x + i, y] in ["O"]):
                full_box = True
            if nseo == "E" and ((y + size) > 10 or self.tablero[x, y + i] in ["O"]):
                full_box = True
            if nseo == "O" and ((y - size + 1) < 0 or self.tablero[x, y - i] in ["O"]):
                full_box = True
        return full_box
    
    
    def init_tablero_aleatorio(self):
        crucero, fragata, destructor, acorazado = 0, 0, 0, 0

        while crucero < 4 or fragata < 3 or destructor < 2 or acorazado < 1:
            if crucero < 4:
                nseo = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.full_box(1, nseo, coordX, coordY):
                    self.introducir_barco(1, nseo, coordX, coordY)
                    crucero += 1
            if fragata < 3:
                nseo = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.full_box(2, nseo, coordX, coordY):
                    self.introducir_barco(2, nseo, coordX, coordY)
                    fragata += 1
            if destructor < 2:
                nseo = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.full_box(3, nseo, coordX, coordY):
                    self.introducir_barco(3, nseo, coordX, coordY)
                    destructor += 1
            if acorazado < 1:
                nseo = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.full_box(4,nseo, coordX, coordY):
                    self.introducir_barco(4, nseo, coordX, coordY)
                    acorazado += 1
                    