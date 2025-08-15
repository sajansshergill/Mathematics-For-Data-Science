import numpy as np

# Fake 2x2 grayscale images
img1 = np.array([[100, 150],
                 [200, 250]])

img2 = np.array([[50, 80],
                 [120, 150]])

# Blend images (vector addition per pixel)
blended_img = img1 + img2
print("Blended Image:\n", blended_img)
