# Definimos una red como un diccionario
# Cada nodo tiene: padres (quién lo afecta) e hijos (a quién afecta)
red = {
    'Clima': {
        'padres': [],
        'hijos': ['Riego', 'Suelo']
    },
    'Riego': {
        'padres': ['Clima'],
        'hijos': ['Suelo']
    },
    'Suelo': {
        'padres': ['Clima', 'Riego'],
        'hijos': []
    }
}


def manto_markov(nodo, red):

    # Padres: nodos que influyen directamente en este
    padres = red[nodo]['padres']

    # Hijos: nodos que dependen de este
    hijos = red[nodo]['hijos']

    # Padres de los hijos (otros nodos relacionados indirectamente)
    padres_hijos = []
    for hijo in hijos:
        for p in red[hijo]['padres']:
            if p != nodo and p not in padres_hijos:
                padres_hijos.append(p)

    # El manto incluye todo lo que rodea al nodo
    manto = set(padres + hijos + padres_hijos)

    return manto


nodo = input("Ingresa el nodo: ")

if nodo in red:
    resultado = manto_markov(nodo, red)
    print("\nManto de Markov de", nodo, ":", resultado)
else:
    print("Ese nodo no existe")