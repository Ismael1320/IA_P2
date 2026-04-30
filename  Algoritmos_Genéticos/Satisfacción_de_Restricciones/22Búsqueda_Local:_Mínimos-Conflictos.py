import random

def conflictos(tablero, col, fila):
    conflictos = 0
    for c in range(len(tablero)):
        if c == col:
            continue
        f = tablero[c]

        if f == fila or abs(f - fila) == abs(c - col):
            conflictos += 1
    return conflictos

def min_conflicts(n, max_pasos=1000):
    tablero = [random.randint(0, n-1) for _ in range(n)]

    for paso in range(max_pasos):
        print("Paso", paso, ":", tablero)

        if all(conflictos(tablero, col, tablero[col]) == 0 for col in range(n)):
            print("Solución encontrada:", tablero)
            return tablero

        columnas_conflicto = [c for c in range(n) if conflictos(tablero, c, tablero[c]) > 0]
        col = random.choice(columnas_conflicto)


        mejor_fila = min(range(n), key=lambda f: conflictos(tablero, col, f))

        tablero[col] = mejor_fila

    print("No se encontró solución")
    return None


n = int(input("Número de reinas (n): "))

min_conflicts(n)