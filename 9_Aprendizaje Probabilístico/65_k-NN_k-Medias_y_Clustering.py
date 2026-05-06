#-------K-NN-----------
# Clasificamos un punto según sus vecinos más cercanos
datos = [
    (1, 'A'),
    (2, 'A'),
    (8, 'B'),
    (9, 'B')
]

nuevo = 3  # dato a clasificar


def knn(k=3):

    # Calculamos distancia
    distancias = []
    for valor, clase in datos:
        distancias.append((abs(valor - nuevo), clase))

    # Ordenamos por cercanía
    distancias.sort()

    # Tomamos los k más cercanos
    vecinos = distancias[:k]

    # Contamos clases
    conteo = {}
    for _, clase in vecinos:
        conteo[clase] = conteo.get(clase, 0) + 1

    # Elegimos la mayoría
    return max(conteo, key=conteo.get)


print("Clasificación:", knn())

#---------K-MEDIAS-------

# Agrupamos datos en 2 grupos
datos = [1, 2, 3, 8, 9, 10]

c1 = 2
c2 = 9


def kmeans():

    global c1, c2

    for _ in range(3):

        g1 = []
        g2 = []

        for d in datos:
            if abs(d - c1) < abs(d - c2):
                g1.append(d)
            else:
                g2.append(d)

        # Actualizamos centros
        c1 = sum(g1) / len(g1)
        c2 = sum(g2) / len(g2)

    return g1, g2


print("Grupos:", kmeans())

#--------CLUSTERING------------

# Solo agrupamos por cercanía sin algoritmo complejo
datos = [1, 2, 3, 10, 11, 12]

grupo1 = []
grupo2 = []

for d in datos:
    if d < 6:
        grupo1.append(d)
    else:
        grupo2.append(d)

print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)