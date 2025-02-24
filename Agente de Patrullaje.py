import random
import time

class Entorno:
    def __init__(self, ruta, obstaculos):
        self.ruta = ruta
        self.obstaculos = obstaculos

    def hay_obstaculo(self, posicion):
        return posicion in self.obstaculos

class AgentePatrullaje:
    def __init__(self, entorno):
        self.entorno = entorno
        self.posicion = 0
        self.direccion = 1

    def mover(self):
        while True:
            if self.entorno.hay_obstaculo(self.posicion):
                print(f"Obstáculo detectado en la posición {self.posicion}. Eliminando obstáculo y continuando.")
                self.entorno.obstaculos.remove(self.posicion)
            else:
                self.posicion += self.direccion
                if self.posicion >= len(self.entorno.ruta):
                    self.posicion = 0
                elif self.posicion < 0:
                    self.posicion = len(self.entorno.ruta) - 1
                print(f"Agente se mueve a la posición {self.posicion}.")
            time.sleep(1)

ruta = list(range(10))
obstaculos = [3, 7]

entorno = Entorno(ruta, obstaculos)
agente = AgentePatrullaje(entorno)

agente.mover()
