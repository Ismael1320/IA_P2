import random

# Calcular fitness del individuo
def fitness(individuo):

    # Sumar los valores del individuo
    return sum(individuo)


# Crear individuo aleatorio
def crear_individuo(tamano):

    return [random.randint(0, 1) for _ in range(tamano)]


# Realizar cruce entre dos padres
def cruce(padre1, padre2):

    # Elegir punto de cruce
    punto = random.randint(1, len(padre1) - 1)

    # Crear hijo combinando ambos padres
    hijo = padre1[:punto] + padre2[punto:]

    return hijo


# Aplicar mutación al individuo
def mutacion(individuo, prob=0.1):

    # Recorrer genes del individuo
    for i in range(len(individuo)):

        # Cambiar gen según probabilidad
        if random.random() < prob:
            individuo[i] = 1 - individuo[i]

    return individuo


# Seleccionar mejores individuos
def seleccion(poblacion):

    # Ordenar por fitness
    poblacion.sort(key=fitness, reverse=True)

    # Retornar los 2 mejores
    return poblacion[:2]


# Algoritmo genético
def algoritmo_genetico(tamano=5, poblacion_size=6, generacion=10):

    # Crear población inicial
    poblacion = [
        crear_individuo(tamano)
        for _ in range(poblacion_size)
    ]

    # Ejecutar generaciones
    for _ in range(generacion):

        # Seleccionar padres
        padres = seleccion(poblacion)

        # Crear nueva población
        nueva_poblacion = padres.copy()

        # Generar hijos
        while len(nueva_poblacion) < poblacion_size:

            hijo = cruce(
                random.choice(padres),
                random.choice(padres)
            )

            # Aplicar mutación
            hijo = mutacion(hijo)

            nueva_poblacion.append(hijo)

        # Actualizar población
        poblacion = nueva_poblacion

    # Obtener mejor individuo
    mejor = max(poblacion, key=fitness)

    return mejor, fitness(mejor)


# Pedir datos al usuario
tamano = int(input("Tamaño del individuo: "))
generacion = int(input("Número de generaciones: "))

# Ejecutar algoritmo genético
mejor, valor = algoritmo_genetico(
    tamano,
    generacion=generacion
)

# Mostrar resultados
print("Mejor individuo:", mejor)
print("Fitness:", valor)