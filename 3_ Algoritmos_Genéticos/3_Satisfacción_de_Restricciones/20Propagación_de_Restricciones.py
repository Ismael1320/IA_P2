def  es_valido(variable, valor , asignacion, grafo):
        for vecino in grafo[variable]:
            if vecino in asignacion and asignacion[vecino] == valor:
                return False
        return True

def propagacion(asignacion, dominios, grafo):
    for var in asignacion:
          valor = asignacion[var]
          for vecino in grafo[var]:
               if vecino not in asignacion:
                    if valor in dominios[vecino]:
                         dominios[vecino].remove(valor)

                         if len(dominios[vecino]) == 0:
                            return False
    return True

def backtracking(asignacion, dominios, grafo):
     if len(asignacion) == len(grafo):
          return asignacion
     
     for var in grafo:
          if var not in asignacion:
               break
          
     for valor in dominios[var]:
          if es_valido(var, valor, asignacion, grafo):
               nueva_asignacion = asignacion.copy()
               nueva_asignacion[var] = valor

               nuevos_dominios = {v: dominios[v][:] for v in dominios}

               if propagacion(nueva_asignacion, nuevos_dominios, grafo):
                    resultado = backtracking(nueva_asignacion, nuevos_dominios, grafo)

                    if resultado:
                         return resultado
     return None

grafo = {
    'A': ['B','C'],
    'B': ['A','C'],
    'C': ['A', 'B']
}

colores = ['Rojo', 'Verde', 'Azul']

dominios = {var: colores[:] for var in grafo}

resultado = backtracking({}, dominios, grafo)

print("Resultado: ", resultado)