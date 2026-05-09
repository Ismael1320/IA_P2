# Verificar si un color es válido para un nodo
def es_valido(nodo, color, asignacion, grafo):

    # Revisar vecinos del nodo
    for vecino in grafo[nodo]:

        # Verificar si un vecino tiene el mismo color
        if vecino in asignacion and asignacion[vecino] == color:
            return False

    return True


# Algoritmo de backtracking
def backtracking(asignacion, grafo, colores):

    # Verificar si todos los nodos tienen color
    if len(asignacion) == len(grafo):
        return asignacion

    # Seleccionar nodo sin asignar
    nodo = next(n for n in grafo if n not in asignacion)

    # Probar cada color disponible
    for color in colores:

        # Verificar si el color es válido
        if es_valido(nodo, color, asignacion, grafo):

            # Asignar color al nodo
            asignacion[nodo] = color

            # Llamada recursiva
            resultado = backtracking(
                asignacion,
                grafo,
                colores
            )

            # Retornar solución encontrada
            if resultado:
                return resultado

            # Quitar asignación si no funciona
            del asignacion[nodo]

    # Retornar None si no hay solución
    return None


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Mostrar información
print("Nodos:", list(grafo.keys()))
print("Colores disponibles:", colores)

# Ejecutar backtracking
resultado = backtracking({}, grafo, colores)

# Mostrar resultado
if resultado:

    print("Asignación válida:")

    for nodo, color in resultado.items():
        print(nodo, "->", color)

else:
    print("No hay solución")