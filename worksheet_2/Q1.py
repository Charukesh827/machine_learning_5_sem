import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define the data (including an outlier)
X = np.array([2,3,5,7,9])
Y = np.array([4,5,7,10,15])

# Calculate the correlation coefficient

corr_coef = np.corrcoef(X, Y)[0, 1]
print(np.corrcoef(X,Y))
print(f"Correlation Coefficient: {corr_coef}")

# Calculate linear regression parameters (slope and intercept)
slope, intercept, r_value, p_value, std_err = linregress(X, Y)
print(f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"R-squared value: {r_value**2:.4f}")

# Calculate predicted Y values
Y_pred = slope * X + intercept

# Calculate residuals (errors)
residuals = Y - Y_pred

# Calculate the least squares of errors
least_squares = np.sum(residuals**2)
print(f"Least Squares of Errors: {least_squares:.2f}")

# Plot the data points and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, Y_pred, color='red', label='Linear regression line')
plt.title('Linear Regression and Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

# Box plot to detect outliers
plt.figure(figsize=(8, 6))
plt.boxplot(Y)
plt.title('Box Plot of Y to Detect Outliers')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Inference on outliers
Q1 = np.percentile(Y, 25)
Q3 = np.percentile(Y, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = (Y < lower_bound) | (Y > upper_bound)
print(f"Number of outliers: {np.sum(outliers)}")
print(f"Outliers: {Y[outliers]}")

if np.sum(outliers) > 0:
    print("There are outliers present in the data.")
else:
    print("No outliers detected in the data.")
