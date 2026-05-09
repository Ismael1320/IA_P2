import random

# Calcular conflictos de una reina
def conflictos(tablero, col, fila):

    conflictos = 0

    # Recorrer columnas del tablero
    for c in range(len(tablero)):

        # Ignorar la misma columna
        if c == col:
            continue

        f = tablero[c]

        # Verificar conflictos en fila o diagonal
        if f == fila or abs(f - fila) == abs(c - col):
            conflictos += 1

    return conflictos


# Algoritmo Min-Conflicts
def min_conflicts(n, max_pasos=1000):

    # Crear tablero inicial aleatorio
    tablero = [
        random.randint(0, n - 1)
        for _ in range(n)
    ]

    # Ejecutar pasos de búsqueda
    for paso in range(max_pasos):

        print("Paso", paso, ":", tablero)

        # Verificar si existe solución
        if all(
            conflictos(tablero, col, tablero[col]) == 0
            for col in range(n)
        ):

            print("Solución encontrada:", tablero)
            return tablero

        # Obtener columnas con conflictos
        columnas_conflicto = [
            c for c in range(n)
            if conflictos(tablero, c, tablero[c]) > 0
        ]

        # Elegir columna aleatoria con conflicto
        col = random.choice(columnas_conflicto)

        # Buscar la mejor fila para reducir conflictos
        mejor_fila = min(
            range(n),
            key=lambda f: conflictos(tablero, col, f)
        )

        # Mover reina a la mejor fila
        tablero[col] = mejor_fila

    # Mostrar mensaje si no se encuentra solución
    print("No se encontró solución")

    return None


# Pedir tamaño del tablero
n = int(input("Número de reinas (n): "))

# Ejecutar algoritmo Min-Conflicts
min_conflicts(n)