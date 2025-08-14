# house price prediction using two features
# 2D Example: House Size + Number of Rooms vs. Price

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example data
house_size = np.array([500, 750, 1000, 1250, 1500])
num_rooms = np.array([2, 3, 3, 4, 4])
house_price = np.array([150, 200, 250, 300, 350])

# Plot 2D input (matrix) with 1D output
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(house_size, num_rooms, house_price, c='red', marker='o')
ax.set_title("House Size & Rooms vs. Price (2D)")
ax.set_xlabel("Size (sq ft)")
ax.set_ylabel("Number of Rooms")
ax.set_zlabel("Price ($1000s)")

plt.show()
