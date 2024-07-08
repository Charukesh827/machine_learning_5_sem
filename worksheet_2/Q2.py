import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
temperature = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2])
sales = np.array([215,325,185,332,406,522,412,614,544,421,445,408])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(temperature, sales)

# Equation of the line
line_eq = f'y = {slope:.2f}x + {intercept:.2f}'
print("Equation of the line of best fit:", line_eq)

# Scatter plot of the data and line of best fit
plt.figure(figsize=(8, 6))
plt.scatter(temperature, sales, color='blue', label='Data points')
plt.plot(temperature, intercept + slope * temperature, color='red', label='Line of best fit')
plt.title('Scatter Plot with Line of Best Fit')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# Interpolation and extrapolation
temperature_interpolate = 21
temperature_extrapolate = 29

# Predict sales at 21°C (interpolation)
sales_interpolate = slope * temperature_interpolate + intercept
print(f"Interpolated sales at {temperature_interpolate}°C: {sales_interpolate:.2f}")

# Predict sales at 29°C (extrapolation)
sales_extrapolate = slope * temperature_extrapolate + intercept
print(f"Extrapolated sales at {temperature_extrapolate}°C: {sales_extrapolate:.2f}")
