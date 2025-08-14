# 1D Example with Regression Line
# a simple linear regression using NumPy’s polyfit and plot the regression line.

import numpy as np
import matplotlib.pyplot as plt

# Data
house_size = np.array([500, 750, 1000, 1250, 1500])
house_price = np.array([150, 200, 250, 300, 350])

# Fit a line: y = m*x + b
m, b = np.polyfit(house_size, house_price, 1)

# Generate predicted values
line = m * house_size + b

# Plot
plt.scatter(house_size, house_price, color='blue', label="Data Points")
plt.plot(house_size, line, color='red', label="Best Fit Line")
plt.title("House Size vs. Price (1D Regression)")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.legend()
plt.grid(True)
plt.show()
