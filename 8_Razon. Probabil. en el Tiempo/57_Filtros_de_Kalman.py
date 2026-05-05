# Estimación inicial
estimacion = 10

# Incertidumbre inicial
incertidumbre = 1

# Medición nueva
medicion = 12

# Ruido de la medición
ruido_medicion = 2


def kalman(estimacion, incertidumbre, medicion, ruido):

    # Calculamos cuánto confiar en la medición
    ganancia = incertidumbre / (incertidumbre + ruido)

    # Ajustamos la estimación con la medición
    nueva_estimacion = estimacion + ganancia * (medicion - estimacion)

    # Reducimos la incertidumbre
    nueva_incertidumbre = (1 - ganancia) * incertidumbre

    return nueva_estimacion, nueva_incertidumbre


print("Estimación inicial:", estimacion)
print("Medición:", medicion)

nueva_est, nueva_inc = kalman(estimacion, incertidumbre, medicion, ruido_medicion)

print("\nEstimación ajustada:", round(nueva_est, 2))
print("Nueva incertidumbre:", round(nueva_inc, 2))