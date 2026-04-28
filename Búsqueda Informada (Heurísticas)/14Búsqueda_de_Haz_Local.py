import random

def vecinos(estados):
    resultado = []
    for i in range(len(estados)):
        nuevo = estados.copy()
        nuevo[i] += 1
        resultado.append(nuevo)

        nuevo = estados.copy()
        nuevo[i] -= 1
        resultado.append(nuevo)
    return resultado

def heuristica(estado, objetivo):
    return sum(abs(a - b) for a, b in zip(estado, objetivo))

def haz_local(inicio, objetivo, k):
    estados =[inicio]

    for _ in range(k -1):
        estados.append([random.randint(0, 10) for _ in range(len(inicio))])

    for paso in range(20):
        print("Paso", paso, ":", estados)

        for e in estados:
            if e == objetivo:
                print ("Encontrado: ", e)
                return
            
        todos = []
        for e in estados:
            todos += vecinos(e)

        todos.sort(key=lambda x: heuristica(x, objetivo))

        estados = todos[:k]

    print("No se encontró solución")

n=int(input("Dimensión: "))

inicio = list(map(int, input("Estado inicial: ").split()))
objetivo = list(map(int, input("Estado objetivo: ").split()))
k = int(input("Valor de k: "))

haz_local(inicio, objetivo, k)