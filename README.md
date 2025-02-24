# Agente de Patrullaje

El código representa un agente de patrullaje que recorre una ruta numerada del 0 al 9. Si encuentra un obstáculo en su camino, lo elimina y continúa moviéndose. Cuando llega al final de la ruta, regresa al inicio y repite el proceso. Su movimiento es continuo, actualizándose cada segundo mientras muestra su posición en pantalla.

# Agente de explorador de mapas
El código simula a un agente que explora una cuadrícula de 5x5. Comienza en la esquina superior izquierda y se mueve de forma aleatoria, eligiendo direcciones como arriba, abajo, izquierda o derecha. Solo avanza si la nueva posición es válida y no ha sido visitada antes. A medida que explora, marca los lugares que ya ha visitado. El agente sigue moviéndose hasta que no puede avanzar más.

# Agente de navegación autónoma
Este código ayuda a encontrar el camino más corto dentro de un laberinto, evitando paredes y eligiendo la mejor ruta posible. Imagina que tienes un mapa con pasillos y obstáculos, donde debes moverte desde un punto de inicio hasta un destino. Para hacerlo, el programa usa una estrategia inteligente llamada A*, que prioriza los caminos más cortos y eficientes. A medida que avanza, va guardando qué pasos tomó para poder reconstruir el camino final. Si encuentra una ruta, la muestra marcando el recorrido con `*`, y si no hay forma de llegar, simplemente lo indica.

# Agente de selección de rutas