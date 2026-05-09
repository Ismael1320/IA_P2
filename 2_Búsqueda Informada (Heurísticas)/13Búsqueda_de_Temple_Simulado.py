import random
import math

# Algoritmo Simulated Annealing
def simulated_annealing(
    grafo,
    inicio,
    objetivo,
    heuristica,
    temp_inicial=10,
    enfriamiento=0.9,
    iteraciones=20
):

    # Nodo actual y mejor nodo encontrado
    actual = inicio
    mejor = actual

    # Guardar el camino recorrido
    camino = [actual]

    # Temperatura inicial
    temperatura = temp_inicial

    # Ejecutar iteraciones
    for _ in range(iteraciones):

        # Detener si se llega al objetivo
        if actual == objetivo:
            break

        # Obtener vecinos del nodo actual
        vecino = grafo[actual]

        # Verificar si no hay vecinos
        if not vecino:
            break

        # Elegir un vecino aleatorio
        siguiente = random.choice(vecino)[0]

        # Calcular diferencia heurística
        delta = heuristica[siguiente] - heuristica[actual]

        # Aceptar mejor solución
        if delta < 0:
            actual = siguiente

        else:
            # Calcular probabilidad de aceptar una peor solución
            prob = math.exp(-delta / temperatura)

            if random.random() < prob:
                actual = siguiente

        # Guardar nodo recorrido
        camino.append(actual)

        # Actualizar mejor nodo encontrado
        if heuristica[actual] < heuristica[mejor]:
            mejor = actual

        # Reducir temperatura
        temperatura *= enfriamiento

        # Detener si la temperatura es muy baja
        if temperatura < 0.01:
            break

    # Retornar camino y mejor nodo encontrado
    return camino, mejor


# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('A', 1)],
    'E': [('F', 1)],
    'F': []
}

# Valores heurísticos
heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Mostrar nodos disponibles
print("Nodos disponibles:", list(grafo.keys()))

# Pedir datos al usuario
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

# Ejecutar Simulated Annealing
camino, mejor = simulated_annealing(
    grafo,
    inicio,
    objetivo,
    heuristica
)

# Mostrar resultados
print("Camino recorrido:", camino)
print("Mejor nodo encontrado:", mejor)