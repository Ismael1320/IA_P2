import random

def fitness(individuo):
    return sum(individuo)

def crear_individuo(tamano):
    return[random.randint(0, 1) for _ in range(tamano)]

def cruce(padre1, paddre2):
    punto = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto] + paddre2[punto:]
    return hijo

def mutuacion(individuo, prob=0.1):
    for i in range(len(individuo)):
        if random.random() < prob:
            individuo[i] = 1 - individuo[i]
        return individuo
    
def seleccion(poblacion):
    poblacion.sort(key=fitness, reverse=True)
    return poblacion [:2]

def algoritmo_generico(tamano=5, poblacion_size=6, generacion=10):
    poblacion = [crear_individuo(tamano) for _ in range(poblacion_size)]

    for _ in range(generacion):
        padres = seleccion(poblacion)

        nueva_poblacion = padres.copy()

        while len(nueva_poblacion) < poblacion_size:
            hijo = cruce(random.choice(padres), random.choice(padres))
            hijo = mutuacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    mejor = max(poblacion, key=fitness)
    return mejor, fitness(mejor)

tamano = int(input("Tamaño del individuo: "))
generacion = int(input("Número de generación: "))

mejor, valor = algoritmo_generico(tamano, generacion=generacion)


print("Mejor individuo: ", mejor)
print("Fitness: ", valor)