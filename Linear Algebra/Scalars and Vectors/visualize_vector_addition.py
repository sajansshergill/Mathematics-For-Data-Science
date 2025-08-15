import numpy as np
import matplotlib.pyplot as plt

# Define two 2D vectors
A = np.array([2, 1])
B = np.array([1, 2])
C = A + B

# Plot vectors
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label="A")
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b', label="B")
plt.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1, color='g', label="A+B")

# Formatting
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.grid(True)
plt.show()
