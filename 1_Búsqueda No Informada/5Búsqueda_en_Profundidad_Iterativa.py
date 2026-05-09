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

        # Evitar repetir nodos
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

            # Retornar el resultado si se encontró el objetivo
            if resultado is not None:
                return resultado

    return None


# Búsqueda en profundidad iterativa
def iddfs(grafo, inicio, objetivo, max_limite):

    # Probar diferentes límites de profundidad
    for limite in range(max_limite + 1):

        print(f"Buscando con límite = {limite}")

        # Ejecutar DLS con el límite actual
        resultado = dls(grafo, inicio, objetivo, limite)

        # Retornar el camino si se encontró
        if resultado is not None:
            return resultado

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
max_limite = int(input("Límite máximo de profundidad: "))

# Ejecutar la búsqueda IDDFS
resultado = iddfs(grafo, inicio, objetivo, max_limite)

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No se encontró el objetivo")