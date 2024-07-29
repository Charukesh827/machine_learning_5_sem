import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
# Generate random x values
x = np.array(7 * np.random.rand(100, 1) - 3)

# Calculate corresponding y values
y = 13*x**2 + 2*x + 7 + np.random.randn(100, 1)  # Add some noise to the data

#Create polynomial features object
poly_features = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly_features.fit_transform(x)

# Create a linear regression model
model1 = LinearRegression()
model2 = LinearRegression()

# Fit the model to the data
model1.fit(x, y)
model2.fit(x_poly,y)

# Get the coefficients of the model
coeffs = model2.coef_
intercept = model2.intercept_

# Print the coefficients
print("Coefficients:", coeffs)
print("Intercept:", intercept)

y_1= coeffs[0][1]*x**2 + coeffs[0][0]*x + intercept

# Get the predicted y values
y_pred1 = model1.predict(x)
y_pred2 = model2.predict(x_poly)


# Plot the data points and the linear line
plt.scatter(x, y, label='Data points')
# plt.plot(x, y_pred1, color='red', label='Linear model')
plt.plot(x, y_pred2, color='gray', label='polynomial model')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Calculate the performance of the model
mse = mean_squared_error(y, y_pred1)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred1)

print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 score: {r2:.2f}')