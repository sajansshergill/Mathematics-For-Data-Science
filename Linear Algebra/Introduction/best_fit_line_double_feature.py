# 2D Example with Regression Plane
# Now let’s fit a plane for the 2D case (size + rooms → price).

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
house_size = np.array([500, 750, 1000, 1250, 1500])
num_rooms = np.array([2, 3, 3, 4, 4])
house_price = np.array([150, 200, 250, 300, 350])

# Prepare matrix X (add column of 1s for bias term)
X = np.c_[house_size, num_rooms, np.ones(house_size.shape[0])]

# Solve linear regression using Normal Equation: w = (X^T X)^(-1) X^T y
w = np.linalg.inv(X.T @ X) @ X.T @ house_price

# Define plane
xx, yy = np.meshgrid(np.linspace(500,1500,10), np.linspace(2,4,10))
zz = w[0]*xx + w[1]*yy + w[2]

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Scatter data
ax.scatter(house_size, num_rooms, house_price, c='red', marker='o', label="Data Points")

# Regression plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='blue')

ax.set_title("House Size & Rooms vs. Price (2D Regression)")
ax.set_xlabel("Size (sq ft)")
ax.set_ylabel("Number of Rooms")
ax.set_zlabel("Price ($1000s)")
ax.legend()
plt.show()
