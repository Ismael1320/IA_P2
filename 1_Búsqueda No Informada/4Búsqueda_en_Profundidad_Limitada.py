# Búsqueda en profundidad limitada
def dls(grafo, nodo, objetivo, limite, profundidad=0, camino=None):

    # Crear la lista del camino en la primera ejecución
    if camino is None:
        camino = []

    # Agregar el nodo actual al camino
    camino.append(nodo)

    # Verificar si se encontró el objetivo
    if nodo == objetivo:
        return camino

    # Detener la búsqueda si se alcanza el límite
    if profundidad == limite:
        return None

    # Recorrer los vecinos del nodo actual
    for vecino in grafo.get(nodo, []):

        # Evitar visitar nodos repetidos
        if vecino not in camino:

            # Llamada recursiva aumentando la profundidad
            resultado = dls(
                grafo,
                vecino,
                objetivo,
                limite,
                profundidad + 1,
                camino.copy()
            )

            # Retornar el camino si se encontró el objetivo
            if resultado is not None:
                return resultado

    # Retornar None si no se encontró el objetivo
    return None


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': [],
}

# Pedir datos al usuario
inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")
limite = int(input("Límite de profundidad: "))

# Ejecutar la búsqueda
resultado = dls(grafo, inicio, objetivo, limite)

print("\nResultado:")

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No se encontró el objetivo dentro del límite")