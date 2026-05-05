def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
        return True
    
def backtracking(asignacion, grafo, colores):
    if len(asignacion) == len(grafo):
         return asignacion
        
    nodo = next(n for n in grafo if n not in asignacion)

    for color in colores:
            if es_valido(nodo, color, asignacion, grafo):
                asignacion[nodo] = color

                resultado = backtracking(asignacion, grafo, colores)
                if resultado:
                    return resultado
                
                del asignacion[nodo]

    return None

grafo = {
    'A': ['B','C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

colores = ['Rojo', 'Verde', 'Azul']

print("Nodos: ", list(grafo.keys()))
print("Colores disponibles: ", list(colores))

resultado = backtracking({}, grafo, colores)

if resultado:
        print("Asignación válida: ")
        for nodo, color in resultado.items():
            print(nodo, " -> ", color)
else:
        print("No hay camino")