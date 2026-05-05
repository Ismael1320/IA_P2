import random
import math

def simulated_annealing(grafo, inicio, objetivo, heuristica, temp_inicial = 10, enfriamiento = 0.9, iteraciones = 20):
    actual = inicio
    mejor = actual
    camino = [actual]
    temperatura = temp_inicial

    for _ in range(iteraciones):
        if actual == objetivo:
            break

        vecino = grafo[actual]
        if not vecino:
            break

        siguiente = random.choice(vecino)[0]

        delta = heuristica[siguiente] - heuristica[actual]

        if delta < 0:
            actual = siguiente
        else:
            prob = math.exp(-delta / temperatura)
            if random.random() < prob:
                actual = siguiente

        camino.append(actual)

        if heuristica[actual] < heuristica[mejor]:
            mejor = actual

        temperatura *= enfriamiento

        if temperatura < 0.01:
            break

    return camino, mejor

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('A', 1)],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

print("Nodos disponibles: ", list(grafo.keys()))
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

camino, mejor = simulated_annealing(grafo, inicio, objetivo, heuristica)


print("Camino recorrido: ", camino)
print("Mejor nodo encontrado: ", mejor)