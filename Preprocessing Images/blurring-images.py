
# load images
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image as grayscale
image = cv2.imread('images/plane.jpg', cv2.IMREAD_GRAYSCALE)

# blur images
image_blurry = cv2.blur(image, (5,5))

# show images
plt.imshow(image_blurry, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.imshow()
