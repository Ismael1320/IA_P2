# Base de datos sencilla
documentos = [
    "python",
    "aprendizaje",
    "redes neuronales",
    "busqueda de datos"
]

# Palabra que queremos buscar
consulta = "redes"


def buscar(consulta, documentos):

    resultados = []

    # Revisamos cada documento
    for doc in documentos:

        # Si la palabra aparece en el texto, guardamos ese documento
        if consulta in doc:
            resultados.append(doc)

    return resultados



resultado = buscar(consulta, documentos)

print("Consulta:", consulta)

print("\nResultados encontrados:\n")

for r in resultado:
    print("-", r)