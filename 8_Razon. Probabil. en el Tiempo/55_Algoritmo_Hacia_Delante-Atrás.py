# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Creencia inicial
inicio = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de observación
observacion = {
    'Soleado': 0.2,
    'Lluvioso': 0.9
}


def normalizar(dist):
    total = sum(dist.values())
    for k in dist:
        dist[k] /= total
    return dist


def forward(creencia):
    # Usamos la información hacia adelante
    nueva = {}
    for s in estados:
        nueva[s] = creencia[s] * observacion[s]
    return normalizar(nueva)


def backward():
    # Aquí solo regresamos valores iguales
    return {'Soleado': 1, 'Lluvioso': 1}


def combinar(f, b):
    # Mezclamos forward y backward
    nueva = {}
    for s in estados:
        nueva[s] = f[s] * b[s]
    return normalizar(nueva)


print("Inicial:", inicio)

f = forward(inicio)
print("Forward:", {k: round(v,2) for k,v in f.items()})

b = backward()
print("Backward:", b)

resultado = combinar(f, b)
print("Resultado:", {k: round(v,2) for k,v in resultado.items()})