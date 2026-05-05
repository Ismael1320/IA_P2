# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Creencia inicial
creencia = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de observar suelo mojado
observacion = {
    'Soleado': 0.2,
    'Lluvioso': 0.9
}


def normalizar(dist):
    total = sum(dist.values())
    for k in dist:
        dist[k] /= total
    return dist


def filtrado(creencia):
    # Ajustamos la creencia con la evidencia
    nueva = {}
    for s in estados:
        nueva[s] = creencia[s] * observacion[s]
    return normalizar(nueva)


def prediccion(creencia):
    # Aquí solo copiamos la creencia
    return creencia


def suavizado(creencia1, creencia2):
    # Mezclamos dos creencias
    nueva = {}
    for s in estados:
        nueva[s] = creencia1[s] * creencia2[s]
    return normalizar(nueva)


def explicacion(creencia):
    # Elegimos el estado más probable
    return max(creencia, key=creencia.get)


print("Inicial:", creencia)

pred = prediccion(creencia)
print("Predicción:", pred)

filt = filtrado(creencia)
print("Filtrado:", {k: round(v,2) for k,v in filt.items()})

suav = suavizado(creencia, filt)
print("Suavizado:", {k: round(v,2) for k,v in suav.items()})

mejor = explicacion(filt)
print("Explicación:", mejor)