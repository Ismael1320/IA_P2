from PIL import Image
from PIL import ImageDraw

# Creamos una imagen blanca
imagen = Image.new("RGB", (400, 300), "white")

# Herramienta para dibujar
dibujo = ImageDraw.Draw(imagen)


# ---------------- SOMBRA ----------------
# Primero dibujamos una sombra gris ligeramente desplazada

dibujo.rectangle(
    (110, 110, 260, 220),
    fill="gray"
)

# Luego dibujamos el objeto principal
dibujo.rectangle(
    (100, 100, 250, 210),
    fill="blue"
)


# ---------------- TEXTURA ----------------
# Dibujamos líneas dentro del rectángulo para simular una textura

for i in range(100, 250, 10):

    dibujo.line(
        (i, 100, i, 210),
        fill="white"
    )


# Guardamos la imagen final
imagen.save("textura_sombra.png")

print("Imagen creada correctamente")