import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

start_time = 28000
input_data = [
    {
        'sunrise_duration': 2100,
        'sunset_duration': 3300,
        'max_i': 200
    },
    {
        'sunrise_duration': 2400,
        'sunset_duration': 3000,
        'max_i': 210
    },
    {
        'sunrise_duration': 2700,
        'sunset_duration': 2700,
        'max_i': 220
    },
    {
        'sunrise_duration': 3000,
        'sunset_duration': 2400,
        'max_i': 220
    },
    {
        'sunrise_duration': 3300,
        'sunset_duration': 2100,
        'max_i': 230
    },
    {
        'sunrise_duration': 3600,
        'sunset_duration': 1800,
        'max_i': 245
    },
    {
        'sunrise_duration': 3300,
        'sunset_duration': 2100,
        'max_i': 245
    },
    {
        'sunrise_duration': 3000,
        'sunset_duration': 2400,
        'max_i': 245
    },
    {
        'sunrise_duration': 2700,
        'sunset_duration': 2700,
        'max_i': 230
    },
    {
        'sunrise_duration': 2400,
        'sunset_duration': 3000,
        'max_i': 220
    },
    {
        'sunrise_duration': 2100,
        'sunset_duration': 3300,
        'max_i': 210
    },
    {
        'sunrise_duration': 1800,
        'sunset_duration': 3600,
        'max_i': 200
    }
]

coefficients = []


# Cubic polynomial function
def poly_func(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


for month in input_data:
    month_results = []

    for key, value in list(month.items())[:-1]:
        x_data = np.array([
            start_time,
            int(start_time + value * 0.25),
            int(start_time + value * 0.37),
            int(start_time + value * 0.50),
            int(start_time + value * 0.75),
            start_time + value
        ])

        y_data = np.array([
            1 if key == 'sunrise_duration' else month['max_i'],
            int(month['max_i'] * 0.046) if key == 'sunrise_duration' else int(month['max_i'] * 0.455),
            int(month['max_i'] * 0.094) if key == 'sunrise_duration' else int(month['max_i'] * 0.138),
            int(month['max_i'] * 0.138) if key == 'sunrise_duration' else int(month['max_i'] * 0.094),
            int(month['max_i'] * 0.455) if key == 'sunrise_duration' else int(month['max_i'] * 0.046),
            month['max_i'] if key == 'sunrise_duration' else 1
        ])

        sigma = [0.1, 0.1, 0.2, 0.1, 0.1, 0.1] if key == 'sunrise_duration' else [0.1, 0.1, 0.2, 0.3, 0.1, 0.1]

        # Setting parameters with curve_fit
        params, covariance = curve_fit(poly_func, x_data, y_data, method='trf', sigma=sigma)

        # Append the coefficients of sunrise or sunset
        month_results.append(params.tolist())

    # Append the coefficients of the month
    coefficients.append(month_results)

month_name = 'November'
month_selector = 10     # Select the (month number - 1) e.g., for January is 0
coefficients_selector = 1  # Enter the selector 0 for 'sunrise', 1 for 'sunset' to select the right coefficients
selector = 'sunset_duration'  # Enter the selector 'sunrise_duration', 'sunrise_duration' or 'max_i'

a, b, c, d = coefficients[month_selector][coefficients_selector]  # Coefficients of the polynomial function e.g., month 0 selector 0
new_selector = input_data[month_selector][selector]
new_max_i = input_data[month_selector]['max_i']

x_data = np.array([
    start_time,
    start_time + new_selector * 0.25,
    start_time + new_selector * 0.37,
    start_time + new_selector * 0.50,
    start_time + new_selector * 0.75,
    start_time + new_selector
])

y_data = np.array([
    1 if coefficients_selector == 0 else new_max_i,
    int(new_max_i * 0.046) if coefficients_selector == 0 else int(new_max_i * 0.455),
    int(new_max_i * 0.094) if coefficients_selector == 0 else int(new_max_i * 0.138),
    int(new_max_i * 0.138) if coefficients_selector == 0 else int(new_max_i * 0.094),
    int(new_max_i * 0.455) if coefficients_selector == 0 else int(new_max_i * 0.046),
    new_max_i if coefficients_selector == 0 else 1
])

print(coefficients)
# Evaluate adjusted function
x_values = np.arange(start_time, start_time + new_selector)  # Range of x to graph
y_values_fit = poly_func(x_values, a, b, c, d)  # Fitted yx values

# Graph the results
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_fit, label="Cubic polynomial fit", color="blue")
plt.scatter(x_data, y_data, color="red", label="Key points")
plt.title(f"Cubic polynomial fit for {selector.split('_')[0]} simulation in {month_name}")
plt.xlabel("x (seconds)")
plt.ylabel("y (value)")
plt.grid()
plt.legend()
plt.show()
