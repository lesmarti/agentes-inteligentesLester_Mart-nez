class AgenteSeleccionRutas:
    def __init__(self, matriz_recompensas):
        self.matriz_recompensas = matriz_recompensas
        self.filas = len(matriz_recompensas)
        self.columnas = len(matriz_recompensas[0])
        self.matriz_utilidades = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

    def calcular_utilidades(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz_utilidades[i][j] = self.matriz_recompensas[i][j] + self.obtener_max_utilidad_vecina(i, j)

    def obtener_max_utilidad_vecina(self, i, j):
        vecinos = []
        if i > 0:
            vecinos.append(self.matriz_utilidades[i-1][j])
        if i < self.filas - 1:
            vecinos.append(self.matriz_utilidades[i+1][j])
        if j > 0:
            vecinos.append(self.matriz_utilidades[i][j-1])
        if j < self.columnas - 1:
            vecinos.append(self.matriz_utilidades[i][j+1])
        return max(vecinos) if vecinos else 0

    def encontrar_ruta_optima(self):
        ruta = []
        i, j = 0, 0
        while i < self.filas - 1 or j < self.columnas - 1:
            ruta.append((i, j))
            if i == self.filas - 1:
                j += 1
            elif j == self.columnas - 1:
                i += 1
            else:
                if self.matriz_utilidades[i+1][j] > self.matriz_utilidades[i][j+1]:
                    i += 1
                else:
                    j += 1
        ruta.append((i, j))
        return ruta

    def imprimir_ruta_optima(self):
        ruta = self.encontrar_ruta_optima()
        print("Ruta Óptima:")
        for celda in ruta:
            print(celda, end=" -> ")
        print("Fin")

if __name__ == "__main__":
    matriz_recompensas = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1],
        [0, 6, 1, 2]
    ]
    agente = AgenteSeleccionRutas(matriz_recompensas)
    agente.calcular_utilidades()
    agente.imprimir_ruta_optima()