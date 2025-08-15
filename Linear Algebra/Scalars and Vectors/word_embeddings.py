import numpy as np

# Simplified embeddings
word_king = np.array([0.7, 0.3])
word_man  = np.array([0.6, 0.1])
word_woman = np.array([0.5, 0.4])

# King - Man + Woman ≈ Queen
word_queen = word_king - word_man + word_woman
print("Queen Vector Approximation:", word_queen)
