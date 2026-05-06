datos = [1, 2, 3, 8, 9, 10]

# Elegimos 2 centros iniciales
c1 = 2
c2 = 9


def distancia(a, b):
    return abs(a - b)  # distancia simple


def agrupar():

    global c1, c2

    for _ in range(3):  # pocas iteraciones

        grupo1 = []
        grupo2 = []

        # Paso 1: asignar cada dato al centro más cercano
        for d in datos:
            if distancia(d, c1) < distancia(d, c2):
                grupo1.append(d)
            else:
                grupo2.append(d)

        # Paso 2: actualizar centros
        if grupo1:
            c1 = sum(grupo1) / len(grupo1)
        if grupo2:
            c2 = sum(grupo2) / len(grupo2)

    return grupo1, grupo2


g1, g2 = agrupar()

print("Grupo 1:", g1)
print("Grupo 2:", g2)