import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset
data = pd.read_csv("advertising.csv")

# Display the first few rows of the dataset
print(data.head())

# Extract TV budget and sales data
TV_budget = data['TV']
sales = data['Sales']

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(TV_budget, sales)

# Print the regression results
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Standard Error: {std_err:.4f}")

# Confidence interval for the slope (95% confidence level)
alpha = 0.05  # significance level
n = len(TV_budget)
t_critical = np.abs(stats.t.ppf(alpha/2, n-2))  # two-tailed t-score

std_error_slope = std_err
margin_of_error = t_critical * std_error_slope

confidence_interval = (slope - margin_of_error, slope + margin_of_error)
print(f"Confidence Interval for Slope (95%): {confidence_interval}")

# Plotting the data and the regression line
plt.figure(figsize=(8, 6))
plt.scatter(TV_budget, sales, color='blue', label='Data points')
plt.plot(TV_budget, intercept + slope * TV_budget, color='red', label='Regression line')
plt.title('Relationship between TV Budget and Sales')
plt.xlabel('TV Budget ($)')
plt.ylabel('Sales (units)')
plt.legend()
plt.grid(True)
plt.show()
