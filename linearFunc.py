import matplotlib.pyplot as plt

# Parameters
y0 = 1  # Initial intensity
ymax = 200  # Final intensity
start_time = 68460  # Start time
duration = 900  # Duration in seconds

# Sunrise curve
slope = float(ymax - y0) / duration
intercept = 1 - (slope * start_time)

# Sunset curve
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
