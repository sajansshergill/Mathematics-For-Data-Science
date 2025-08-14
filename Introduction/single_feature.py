# house price prediction using a single feature (number of rooms)
# House Size vs. Price

import numpy as np
import matplotlib.pyplot as plt

# Example data: size of houses (in square feet) and prices (in $1000s)
house_size = np.array([500, 750, 1000, 1250, 1500])
house_price = np.array([150, 200, 250, 300, 350])

# Plot 1D relationship
plt.scatter(house_size, house_price, color='blue', marker='o')
plt.title("House Size vs. Price (1D)")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.grid(True)
plt.show()
