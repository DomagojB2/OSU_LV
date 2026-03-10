import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('LV2/road.jpg')

brightness = 50
brightened_image = np.clip(img.astype(np.uint16) + brightness, 0, 255).astype(np.uint8)
plt.figure()
plt.imshow(brightened_image)
plt.show()

width = img.shape[1]
second_quarter = width // 2
second_quarter_img = img[:, second_quarter:]
plt.figure()
plt.imshow(second_quarter_img)
plt.show()

rotated_img = np.rot90(img, k = 1)
plt.figure()
plt.imshow(rotated_img)
plt.show()

mirrored_img = np.flip(img, axis = 0)
plt.figure()
plt.imshow(mirrored_img)
plt.show()