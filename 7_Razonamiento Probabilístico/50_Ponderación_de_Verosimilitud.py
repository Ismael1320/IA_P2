import random

#Probabilidad de que algo ocurra
P_lluvia = 0.7

def muestreo_directo(n=10):

    conteo = 0

    for _ in range(n):

        #Generamos un número alatorio
        if random.random() < P_lluvia:
            conteo += 1

    return conteo / n

def muestreo_rechazado(n=10):
    
    aceptadas = 0
    total = 0

    for _ in range(n):

        #Generamos un evento
        valor = random.random()

        #Solo aceptamos valores menores a 0.5(Condición simple)
        if valor < 0.5:
            total+=1

        #Dentro de los aceptados, vemos si ocurre el evento
        if valor < P_lluvia:
            aceptadas +=1

    #Evitar división entre cero
    if total == 0:
        return 0
    
    return aceptadas / total

print("Directo: ", round(muestreo_directo(10), 2))
print("Rechazado: ", round(muestreo_rechazado(10), 2))
