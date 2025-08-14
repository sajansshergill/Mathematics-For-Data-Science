# Showing how to do the same thing with scikit-learn’s LinearRegression (to compare manual linear algebra vs ML library)?

# Scikit-learn versions of the 1D and 2D regressions with visuals
# (Two separate charts; no seaborn; default matplotlib colors.)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# --------------------------
# 1D: Size -> Price
# --------------------------
house_size = np.array([500, 750, 1000, 1250, 1500])
house_price = np.array([150, 200, 250, 300, 350])

# Reshape X to 2D (n_samples, n_features)
X1 = house_size.reshape(-1, 1)
y = house_price

model_1d = LinearRegression()
model_1d.fit(X1, y)

# Predictions on a dense grid for a smooth line
size_grid = np.linspace(house_size.min(), house_size.max(), 100).reshape(-1, 1)
price_pred_1d = model_1d.predict(size_grid)

# Print learned parameters
print("1D LinearRegression")
print(f"  Coefficient (slope) m: {model_1d.coef_[0]:.4f}")
print(f"  Intercept b: {model_1d.intercept_:.4f}")
print(f"  R^2 on training data: {model_1d.score(X1, y):.4f}\n")

# Plot 1D
plt.figure(figsize=(6,4))
plt.scatter(house_size, house_price, label="Data")
plt.plot(size_grid, price_pred_1d, label="Best Fit (sklearn)")
plt.title("House Size vs. Price (1D) — scikit-learn")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.legend()
plt.grid(True)
plt.show()

# --------------------------
# 2D: [Size, Rooms] -> Price
# --------------------------
num_rooms = np.array([2, 3, 3, 4, 4])
X2 = np.column_stack([house_size, num_rooms])

model_2d = LinearRegression()
model_2d.fit(X2, y)

# Create a grid for the regression plane
xx, yy = np.meshgrid(np.linspace(house_size.min(), house_size.max(), 15),
                     np.linspace(num_rooms.min(), num_rooms.max(), 15))
# Flatten the grid and predict
grid_points = np.column_stack([xx.ravel(), yy.ravel()])
zz = model_2d.predict(grid_points).reshape(xx.shape)

# Print learned parameters
print("2D LinearRegression")
print(f"  Coefficients [size, rooms]: {model_2d.coef_[0]:.4f}, {model_2d.coef_[1]:.4f}")
print(f"  Intercept: {model_2d.intercept_:.4f}")
print(f"  R^2 on training data: {model_2d.score(X2, y):.4f}\n")

# Plot 3D with the regression plane
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(house_size, num_rooms, house_price, label="Data")
ax.plot_surface(xx, yy, zz, alpha=0.5)
ax.set_title("Size & Rooms vs. Price (2D) — scikit-learn")
ax.set_xlabel("Size (sq ft)")
ax.set_ylabel("Number of Rooms")
ax.set_zlabel("Price ($1000s)")
# Matplotlib 3D axes don't support the 2D legend the same way; we can skip or use a proxy
plt.show()
