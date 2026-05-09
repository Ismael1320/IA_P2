from PIL import Image
from PIL import ImageDraw

# Creamos una imagen blanca
imagen = Image.new("RGB", (400, 300), "white")

# Herramienta para dibujar
dibujo = ImageDraw.Draw(imagen)

# Dibujamos un rectángulo
dibujo.rectangle(
    (50, 80, 170, 200),
    fill="blue"
)

# Dibujamos un círculo
dibujo.ellipse(
    (230, 80, 350, 200),
    fill="red"
)

# Guardamos imagen original
imagen.save("objetos.png")


# Función para reconocer objetos
def reconocer_objetos():

    objetos = []

    # Revisamos las figuras conocidas
    objetos.append("Rectangulo azul")
    objetos.append("Circulo rojo")

    return objetos



encontrados = reconocer_objetos()

print("Objetos reconocidos:\n")

for obj in encontrados:
    print("-", obj)