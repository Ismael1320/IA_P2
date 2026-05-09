from PIL import Image
from PIL import ImageDraw

# Creamos una imagen blanca
imagen = Image.new("RGB", (300, 200), "white")

# Herramienta para dibujar
dibujo = ImageDraw.Draw(imagen)

# Dibujamos una letra sencilla
dibujo.text((120, 80), "A", fill="black")

# Guardamos la imagen
imagen.save("letra.png")


# Función de reconocimiento simple
def reconocer(letra):

    # Simulamos reconocimiento
    if letra == "A":
        return "Letra reconocida: A"

    else:
        return "No reconocida"


resultado = reconocer("A")

print(resultado)