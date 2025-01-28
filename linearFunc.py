import numpy as np
import matplotlib.pyplot as plt

# Parámetros
y0 = 1  # Intensidad inicial
ymax = 200  # Intensidad final
start_time = 68460  # Tiempo de inicio
duration = 900  # Duración en segundos

slope = float(ymax - y0) / duration
intercept = 1 - (slope * start_time)

# slope = float(ymax - y0) / -duration
# intercept = ymax - (slope * start_time)

x_data = list(range(start_time, start_time + duration))
y_data = [slope * x + intercept for x in x_data]

# Graficar
plt.plot(x_data, y_data)
plt.title("Sunrise lineal intensity control")
plt.xlabel("Time (seconds)")
plt.ylabel("Light intensity")
plt.grid(True)
plt.show()
