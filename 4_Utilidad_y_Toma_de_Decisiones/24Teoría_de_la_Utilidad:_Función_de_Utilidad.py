opciones = {
    'Opcion_A': 100,
    'Opcion_B': 80,
    'Opcion_C': 50
}

def utilidad(valor):
    return valor ** 0.5

def evaluar_opciones():
    mejor = None
    mejor_utilidad = float('-inf')

    for opcion, valor in opciones.items():
        u = utilidad(valor)
        print(f"{opcion} -> Valor: {valor}, Utilidad: {u:.2f}")

        if u > mejor_utilidad:
            mejor_utilidad = u
            mejor = opcion

    return mejor, mejor_utilidad

mejor, u = evaluar_opciones()

print("Mejor opción: ", mejor)
print("Mayor utilidad: ", round(u, 2))
