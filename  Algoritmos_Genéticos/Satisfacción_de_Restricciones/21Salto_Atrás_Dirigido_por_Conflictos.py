def cbj(grafo, colores):
    asignacion = {}
    conflictos = {nodo: set() for nodo in grafo}

    def es_valido(nodo, color):
        for vecino in grafo[nodo]:
            if vecino in asignacion and asignacion[vecino] == color:
                return False, vecino
        return True, None
    
    def reslover(nodos, i=0):
        if i == len(nodos):
            return True 
        
        nodo = nodos[i]

        for color in colores:
            valido, conflictos =  es_valido(nodo, color)

            if valido:
                asignacion[nodo] = color
            
            if reslover(nodos, i + 1):
                return True
            
            del asignacion[nodo]
        else:
            conflictos[nodo].add(conflictos)

        if conflictos[nodo]:
            salto = max(conflictos[nodo], key=lambda x: nodos.index(x))
            return False
        
        return False
    
    nodos = list(grafo.keys())
    reslover(nodos)

    return asignacion

grafo = {
    'A': ['B','C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

colores = ['Rojo', 'Verde', 'Azul']

print("Nodos: ", list(grafo.keys()))
print("Colores: ", list(colores))

resultado = cbj(grafo, colores)

if resultado:
        print("Asignación válida: ")
        for nodo, color in resultado.items():
            print(nodo, " -> ", color)
else:
        print("No hay camino")
