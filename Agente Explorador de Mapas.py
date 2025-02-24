import random

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.posicion_actual = (0, 0)
        self.visitados = {self.posicion_actual}

    def mover(self):
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(movimientos)
        for movimiento in movimientos:
            nueva_posicion = (self.posicion_actual[0] + movimiento[0], self.posicion_actual[1] + movimiento[1])
            if self.es_valida(nueva_posicion) and nueva_posicion not in self.visitados:
                self.posicion_actual = nueva_posicion
                self.visitados.add(nueva_posicion)
                return nueva_posicion
        return None

    def es_valida(self, posicion):
        return 0 <= posicion[0] < self.filas and 0 <= posicion[1] < self.columnas

    def explorar(self):
        while self.mover():
            self.imprimir_entorno()

    def imprimir_entorno(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) == self.posicion_actual:
                    print("A", end=" ")
                elif (i, j) in self.visitados:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print()
        print()

if __name__ == "__main__":
    agente = AgenteExplorador(5, 5)
    agente.explorar()
