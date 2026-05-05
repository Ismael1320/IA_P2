# Lista de decisiones posibles para cada empresa
opciones = ['Alto', 'Bajo']

# Tabla de ganancias: Cada clave es una combinación (Empresa1, Empresa2)
# Mientras que cada valor es una tupla (ganancia_empresa1, ganancia_empresa2)
ganancias = {
    ('Alto', 'Alto'): (8, 8),   # Ambas ponen precio alto
    ('Alto', 'Bajo'): (2, 10),  # Empresa1 alto, Empresa2 bajo
    ('Bajo', 'Alto'): (10, 2),  # Empresa1 bajo, Empresa2 alto
    ('Bajo', 'Bajo'): (5, 5)    # Ambas ponen precio bajo
}

# Función que busca decisiones estables
def encontrar_equilibrio():
    resultados = []

    # Probamos todas las combinaciones posibles de decisiones
    for e1 in opciones:        # decisión de Empresa 1
        for e2 in opciones:    # decisión de Empresa 2

            # Obtenemos la ganancia actual para esa combinación
            actual = ganancias[(e1, e2)]

            # Revisar si Empresa 1 puede mejorar
            mejora1 = False

            # Probamos si Empresa 1 cambia su decisión
            for alt1 in opciones:
                # Comparamos si la ganancia sería mayor
                if ganancias[(alt1, e2)][0] > actual[0]:
                    mejora1 = True   # sí puede mejorar cambiando

            # Revisar si Empresa 2 puede mejorar
            mejora2 = False

            # Probamos si Empresa 2 cambia su decisión
            for alt2 in opciones:
                if ganancias[(e1, alt2)][1] > actual[1]:
                    mejora2 = True

            # Si ninguna puede mejorar → equilibrio
            if not mejora1 and not mejora2:
                resultados.append((e1, e2, actual))

    return resultados




print("Opciones disponibles:", opciones)

# Buscamos decisiones estables
eq = encontrar_equilibrio()

print("\nDecisiones estables encontradas:\n")

# Mostramos resultados
for e1, e2, g in eq:
    print(f"Empresa1: {e1}, Empresa2: {e2} -> Ganancias: {g}")