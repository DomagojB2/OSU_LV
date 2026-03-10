import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((50, 50), dtype=np.uint8) 
white = np.ones((50, 50), dtype=np.uint8) * 255

image = np.vstack((np.hstack((black, white)), np.hstack((white, black))))
plt.figure()
plt.imshow(image, cmap="gray")
plt.show()