import numpy as np
import matplotlib.pyplot as plt

vert = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
hor = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

img = plt.imread('Edge Detection2.jpg')
height, width, num_channels = img.shape
sobel = img.copy()

for i in range(3, height - 2):
    for j in range(3, width - 2):
        pixels = img[i - 1:i + 2, j - 1:j + 2, 0]
        vertT = vert * pixels
        vertical_score = vertT.sum() / 4
        horT = hor * pixels
        horScore = horT.sum() / 4
        sobelScore = (vertical_score ** 2 + horScore ** 2) ** .5
        sobel[i, j] = [sobelScore] * 3
sobel = sobel / sobel.max()

plt.imshow(sobel)
plt.show()
