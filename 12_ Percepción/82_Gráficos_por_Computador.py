import matplotlib.pyplot as plt
import numpy as np

# Generamos valores para el eje X
x = np.linspace(0, 10, 100)

# Funciones matemáticas
y1 = np.sin(x)
y2 = np.cos(x)

# Creamos la figura
plt.figure(figsize=(8, 5))

# Dibujamos las funciones
plt.plot(x, y1, label="Seno")
plt.plot(x, y2, label="Coseno")

# Títulos y etiquetas
plt.title("Graficos por Computador")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Cuadrícula y leyenda
plt.grid(True)
plt.legend()

# Guardamos la imagen
plt.savefig("grafica.png")

print("Imagen guardada como grafica.png")