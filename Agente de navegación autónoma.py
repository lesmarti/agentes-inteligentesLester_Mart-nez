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

