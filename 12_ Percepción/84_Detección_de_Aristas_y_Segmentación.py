from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

# Creamos una imagen blanca
imagen = Image.new("RGB", (300, 300), "white")

# Herramienta para dibujar
dibujo = ImageDraw.Draw(imagen)

# Dibujamos algunas figuras
dibujo.rectangle((50, 50, 140, 140), fill="blue")
dibujo.ellipse((170, 80, 270, 180), fill="red")

# Guardamos imagen original
imagen.save("original.png")

# ---------------- DETECCIÓN DE ARISTAS ----------------
# Este filtro resalta los bordes de las figuras

bordes = imagen.filter(ImageFilter.FIND_EDGES)

# Guardamos resultado
bordes.save("bordes.png")


# ---------------- SEGMENTACIÓN ----------------
# Aquí convertimos la imagen a blanco y negro. Para separar objetos del fondo

gris = imagen.convert("L")

# Creamos una nueva imagen segmentada
segmentada = gris.point(lambda p: 255 if p > 120 else 0)

# Guardamos resultado
segmentada.save("segmentada.png")

print("Procesamiento completado")