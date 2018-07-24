from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    for i in range(5, int(sqrt(n))):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

img = np.zeros((1000,1000))
delta = np.shape(img)[0]
print(np.shape(img))
for x in range(np.shape(img)[0]//2-delta,np.shape(img)[0]//2,1):
    for y in range(np.shape(img)[1]//2-delta,np.shape(img)[1]//2,1):
        if (is_prime(abs(x^y))):
            img[x+delta//2][y+delta//2] = 1


ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.plasma()
plt.imshow(img, interpolation="bicubic")
plt.savefig("figure.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()