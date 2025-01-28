import numpy as np
import matplotlib.pyplot as plt

# Parámetros
y0 = 1  # Intensidad inicial
ymax = 200  # Intensidad final
start_time = 68460  # Tiempo de inicio
duration = 900  # Duración en segundos

# Calculamos la constante k con una mejor fórmula

k = np.log(ymax / y0) / duration  # Ajustar k para que llegue a ymax en el tiempo deseado
print(k)

# Función exponencial
def light_intensity(t):
    return y0 * np.exp(k * t)  # Usamos una exponencial simple para simular el encendido de la luz


# Tiempo desde el segundo start_time hasta start_time + duration
time = np.linspace(start_time, start_time + duration)  # Usamos linspace para obtener 1000 puntos

# Intensidad de la luz en función del tiempo
intensity = light_intensity(time - start_time)  # Ajustamos t para empezar desde 0
# intensity = ymax - (intensity - y0)

print(intensity)
# Graficar
plt.plot(time, intensity)
plt.title(" Sunrise exponential intensity control")
plt.xlabel("Time (seconds)")
plt.ylabel("Light intensity")
plt.grid(True)
plt.show()
