import random

# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Probabilidad inicial
inicio = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de observar mojado
P_obs = {
    'Soleado': 0.2,
    'Lluvioso': 0.9
}


def generar_particulas(n=10):
    particulas = []

    # Creamos varias copias del sistema
    for _ in range(n):
        if random.random() < inicio['Soleado']:
            particulas.append('Soleado')
        else:
            particulas.append('Lluvioso')

    return particulas


def ponderar(particulas):
    pesos = []

    # A cada partícula le damos un peso según la observación
    for p in particulas:
        pesos.append(P_obs[p])

    return pesos


def normalizar(pesos):
    total = sum(pesos)
    return [p / total for p in pesos]


def re_muestrear(particulas, pesos):
    
    nuevas = []

    # Elegimos partículas según su peso
    for _ in particulas:
        r = random.random()
        acumulado = 0

        for i in range(len(particulas)):
            acumulado += pesos[i]
            if r < acumulado:
                nuevas.append(particulas[i])
                break

    return nuevas




# Paso 1: generar partículas
particulas = generar_particulas(10)
print("Partículas iniciales:", particulas)

# Paso 2: asignar pesos
pesos = ponderar(particulas)
pesos = normalizar(pesos)
print("Pesos:", [round(p,2) for p in pesos])

# Paso 3: re-muestreo
nuevas = re_muestrear(particulas, pesos)
print("Partículas nuevas:", nuevas)