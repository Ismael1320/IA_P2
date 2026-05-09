import random

# Generar vecinos del estado actual
def vecinos(estados):

    resultado = []

    # Recorrer cada posición del estado
    for i in range(len(estados)):

        # Crear vecino aumentando 1
        nuevo = estados.copy()
        nuevo[i] += 1
        resultado.append(nuevo)

        # Crear vecino disminuyendo 1
        nuevo = estados.copy()
        nuevo[i] -= 1
        resultado.append(nuevo)

    return resultado


# Calcular distancia al objetivo
def heuristica(estado, objetivo):

    return sum(abs(a - b) for a, b in zip(estado, objetivo))


# Búsqueda online
def busqueda_online(inicio, objetivo, max_pasos=20):

    # Estado actual
    actual = inicio

    # Ejecutar pasos de búsqueda
    for paso in range(max_pasos):

        print("Paso", paso, ":", actual)

        # Verificar si se llegó al objetivo
        if actual == objetivo:
            print("Encontrado:", actual)
            return

        # Generar posibles movimientos
        opciones = vecinos(actual)

        # Elegir la mejor opción según la heurística
        mejor = min(
            opciones,
            key=lambda x: heuristica(x, objetivo)
        )

        # Actualizar estado actual
        actual = mejor

    # Mostrar mensaje si no se encuentra solución
    print("No se encontró solución")


# Pedir datos al usuario
n = int(input("Dimensión: "))

inicio = list(
    map(int, input("Estado inicial: ").split())
)

objetivo = list(
    map(int, input("Estado objetivo: ").split())
)

# Ejecutar búsqueda online
busqueda_online(inicio, objetivo)