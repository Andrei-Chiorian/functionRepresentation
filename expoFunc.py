import numpy as np
import matplotlib.pyplot as plt

# Parameters
y0 = 1  # Initial intensity
ymax = 200  # Final intensity
start_time = 68460  # Tiempo de inicio
duration = 900  # Duration in seconds

# We calculate the constant k with a better formula

k = np.log(ymax / y0) / duration  # Adjust k so that it reaches ymax in the desired time
print(k)

# exponential function
def light_intensity(t):
    return y0 * np.exp(k * t)  # We use a simple exponential to simulate the turning on of the light


# Time from second start_time to start_time + duration
time = np.linspace(start_time, start_time + duration)  # We use linspace to get 1000 points

# Intensidad de la luz en función del tiempo
intensity = light_intensity(time - start_time)  # We adjust t to start from 0
# intensity = ymax - (intensity - y0)

print(intensity)
# Graph
plt.plot(time, intensity)
plt.title(" Sunrise exponential intensity control")
plt.xlabel("Time (seconds)")
plt.ylabel("Light intensity")
plt.grid(True)
plt.show()
