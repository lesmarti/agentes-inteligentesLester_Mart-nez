import heapq

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 2]
]

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_valida(x, y):
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] != 1

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def buscar_ruta(laberinto):
    inicio = (0, 0)
    meta = (4, 4)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)

        if actual == meta:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = padres[actual]
            return ruta[::-1]

        for direccion in direcciones:
            vecino = (actual[0] + direccion[0], actual[1] + direccion[1])
            if es_valida(vecino[0], vecino[1]):
                nuevo_costo = costos[actual] + 1
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(meta, vecino)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    padres[vecino] = actual

    return None

def mostrar_ruta(laberinto, ruta):
    for paso in ruta:
        laberinto[paso[0]][paso[1]] = '*'
    for fila in laberinto:
        print(' '.join(str(c) for c in fila))

ruta = buscar_ruta(laberinto)
if ruta:
    print("Ruta encontrada:")
    mostrar_ruta(laberinto, ruta)
else:
    print("No se encontró una ruta.")
