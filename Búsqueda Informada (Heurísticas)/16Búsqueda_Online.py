import random

def vecinos(estados):
    resultado=[]
    for i in range(len(estados)):
        nuevo = estados.copy()
        nuevo[i] += 1
        resultado.append(nuevo)

        nuevo=estados.copy()
        nuevo[i] -= 1
        resultado.append(nuevo)
    return resultado

def heuristica(estado, objetivo):
    return sum(abs(a - b) for a, b in zip(estado, objetivo))

def busqueda_online(inicio, objetivo, max_pasos=20):
    actual =inicio

    for paso in range(max_pasos):
        print("Paso", paso, ":", actual)

        if actual == objetivo:
            print("Encontrado: ", actual)
            return
        
        opciones = vecinos(actual)

        mejor = min(opciones, key=lambda x: heuristica(x, objetivo))

        actual = mejor

    print("No se encontro solución")

n = int(input("Dimensión: "))

inicio = list(map(int, input("Estado inicial: ").split()))
objetivo = list(map(int, input("Estado objetivo: ").split()))

busqueda_online(inicio, objetivo)  