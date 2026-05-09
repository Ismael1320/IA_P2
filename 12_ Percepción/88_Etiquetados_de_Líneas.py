# Etiquetado de Líneas
# Este ejemplo dibuja líneas y les asigna etiquetas

from PIL import Image
from PIL import ImageDraw

# Creamos una imagen blanca
imagen = Image.new("RGB", (400, 300), "white")

# Herramienta de dibujo
dibujo = ImageDraw.Draw(imagen)


# ---------------- LÍNEA 1 ----------------
# Dibujamos una línea horizontal

dibujo.line(
    (50, 80, 350, 80),
    fill="blue",
    width=3
)

# Agregamos etiqueta
dibujo.text(
    (160, 50),
    "Linea Horizontal",
    fill="black"
)


# ---------------- LÍNEA 2 ----------------
# Dibujamos una línea diagonal

dibujo.line(
    (50, 200, 350, 250),
    fill="red",
    width=3
)

# Agregamos etiqueta
dibujo.text(
    (150, 210),
    "Linea Diagonal",
    fill="black"
)


# Guardamos la imagen
imagen.save("lineas_etiquetadas.png")

print("Imagen generada correctamente")