# Definimos una distribución
# Cada estado tiene una probabilidad asociada
# (esto representa lo que creemos que puede pasar)
distribucion = {
    'Soleado': 0.6,
    'Nublado': 0.3,
    'Lluvioso': 0.1
}


# Función para verificar si la distribución es válida
def verificar_distribucion(dist):

    # Sumamos todas las probabilidades
    total = sum(dist.values())

    # Una distribución válida debe sumar 1
    # Usamos un margen pequeño por si hay decimales
    if abs(total - 1.0) < 0.0001:
        return True
    else:
        return False



# Función para encontrar el evento más probable
def evento_mas_probable(dist):

    # Aquí simplemente buscamos el valor más grande
    # y regresamos el estado que lo tiene
    return max(dist, key=dist.get)



print("Distribución:", distribucion)

# Primero verificamos si todo está bien definido
if verificar_distribucion(distribucion):
        print("La distribución está bien (todo suma 1)")
else:
    print("Ojo: la distribución no suma 1")

# Ahora vemos cuál es el resultado más probable
mejor = evento_mas_probable(distribucion)

print("\nEl resultado más probable es:", mejor)
print("Con una probabilidad de:", distribucion[mejor])