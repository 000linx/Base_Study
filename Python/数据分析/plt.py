import matplotlib.pyplot as plt
import numpy as np
img_arr = plt.imread("1.jpg")
img_arr
print(img_arr)
print(type(img_arr))

img_arr.shape
plt.imshow(img_arr)
plt.show()