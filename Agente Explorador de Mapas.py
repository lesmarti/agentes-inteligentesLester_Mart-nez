import random

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.posicion_actual = (0, 0)
        self.visitados = {self.posicion_actual}
