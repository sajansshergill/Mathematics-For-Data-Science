import numpy as np

# Each row is a vector
vectors = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [0, 2, 4]
])

# Sum across rows
result = np.sum(vectors, axis=0)

print("Vectors:\n", vectors)
print("Sum of vectors =", result)
