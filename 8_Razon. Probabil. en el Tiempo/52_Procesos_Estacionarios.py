import random

# Estados posibles
estados = ['A', 'B']

# Probabilidades de transición
transiciones = {
    'A': {'A': 0.7, 'B': 0.3},  
    'B': {'A': 0.4, 'B': 0.6}
}

def sigiente_estado(estado):

    #Generamos un número para decidir a dónde ir
    r= random.random()

    acumulado = 0
    for destino, prob in transiciones[estado].items():
        acumulado += prob

        #Cuando se pasa del valor aleatorio, elegimos es estado
        if r < acumulado:
            return destino
        
def simular(pasos=50):
    estado = 'A'  # empezamos en A
    conteo = {'A': 0, 'B': 0}

    for _ in range(pasos):

        # Contamos cuantas veces visitamos cada estado
        conteo[estado] += 1

        # Nos movemos al siguiente estado r
        estado = sigiente_estado(estado)

    # Convertimos a proporciones
    total = sum(conteo.values())
    for e in conteo:
        conteo[e] = conteo[e] / total

    return conteo

resultado = simular(100)

print("Distribución aproximada después de muchos pasos: ")
for estado, valor in resultado.items():
    print(estado, "->", round(valor, 2))