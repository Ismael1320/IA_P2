from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw

# Creamos una imagen blanca
imagen = Image.new("RGB", (300, 300), "white")

# Herramienta para dibujar
dibujo = ImageDraw.Draw(imagen)

# Dibujamos algunas figuras
dibujo.rectangle((50, 50, 150, 150), fill="blue")
dibujo.ellipse((170, 70, 270, 170), fill="red")

# Guardamos la imagen original
imagen.save("imagen_original.png")

# Aplicamos filtro de desenfoque
desenfoque = imagen.filter(ImageFilter.BLUR)

# Aplicamos filtro de bordes
bordes = imagen.filter(ImageFilter.FIND_EDGES)

# Guardamos resultados
desenfoque.save("imagen_desenfoque.png")
bordes.save("imagen_bordes.png")

print("Imágenes procesadas correctamente")