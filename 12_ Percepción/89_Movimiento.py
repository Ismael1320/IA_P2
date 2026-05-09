from PIL import Image
from PIL import ImageDraw

# Tamaño de la imagen
ancho = 400
alto = 200

# Creamos varios cuadros (frames)
for i in range(5):

    # Fondo blanco
    imagen = Image.new("RGB", (ancho, alto), "white")

    # Herramienta de dibujo
    dibujo = ImageDraw.Draw(imagen)

    # Posición del objeto
    x = 50 + (i * 50)

    # Dibujamos un círculo moviéndose
    dibujo.ellipse(
        (x, 80, x + 50, 130),
        fill="blue"
    )

    # Texto de referencia
    dibujo.text(
        (140, 20),
        f"Movimiento Frame {i+1}",
        fill="black"
    )

    # Guardamos cada frame
    imagen.save(f"movimiento_{i+1}.png")

print("Frames de movimiento generados")