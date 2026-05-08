# ---------------- HEBB ----------------
# # Aprende aumentando pesos cuando dos valores se activan juntos

x = 1
y = 1

peso_hebb = 0

# Regla de Hebb
peso_hebb = peso_hebb + (x * y)

print("Peso Hebb:", peso_hebb)



# ---------------- HAMMING ----------------
# Calcula diferencias entre dos patrones

patron1 = [1, 0, 1, 1]
patron2 = [1, 1, 0, 1]

distancia = 0

for i in range(len(patron1)):

    if patron1[i] != patron2[i]:
        distancia += 1

print("Distancia Hamming:", distancia)



# ---------------- HOPFIELD ----------------
# Recupera información usando memoria asociativa

entrada = [1, -1, 1]

# Memoria guardada
memoria = [1, -1, 1]

if entrada == memoria:
    print("Hopfield reconoció el patrón")
else:
    print("Hopfield no reconoció el patrón")



# ---------------- BOLTZMANN ----------------
# Usa probabilidad para cambiar estados

import random

estado = 0

# Cambio aleatorio de estado
if random.random() > 0.5:
    estado = 1

print("Estado Boltzmann:", estado)