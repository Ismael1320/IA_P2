import random

# Generar vecinos modificando cada valor
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


# Calcular distancia entre estado y objetivo
def heuristica(estado, objetivo):

    return sum(abs(a - b) for a, b in zip(estado, objetivo))


# Algoritmo de Haz Local
def haz_local(inicio, objetivo, k):

    # Lista inicial de estados
    estados = [inicio]

    # Generar estados aleatorios
    for _ in range(k - 1):
        estados.append(
            [random.randint(0, 10) for _ in range(len(inicio))]
        )

    # Ejecutar pasos de búsqueda
    for paso in range(20):

        print("Paso", paso, ":", estados)

        # Verificar si se encontró el objetivo
        for e in estados:
            if e == objetivo:
                print("Encontrado:", e)
                return

        # Guardar todos los vecinos
        todos = []

        for e in estados:
            todos += vecinos(e)

        # Ordenar según la heurística
        todos.sort(key=lambda x: heuristica(x, objetivo))

        # Seleccionar los mejores k estados
        estados = todos[:k]

    # Mostrar mensaje si no se encuentra solución
    print("No se encontró solución")


# Pedir datos al usuario
n = int(input("Dimensión: "))

inicio = list(map(int, input("Estado inicial: ").split()))
objetivo = list(map(int, input("Estado objetivo: ").split()))

k = int(input("Valor de k: "))

# Ejecutar búsqueda de haz local
haz_local(inicio, objetivo, k)