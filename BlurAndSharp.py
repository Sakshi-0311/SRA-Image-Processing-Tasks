import numpy as np
from PIL import Image, ImageDraw

input_image = Image.open("blur.png")
input_pixels = input_image.load()

# Box-Blur
box = (1/25)*np.ones((5, 5))

# Gaussian Blur
gauss = (1/273)*np.array([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]])

# Sharpen
sharp = (-1)*np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, -25, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])

kernel = gauss

offset = len(kernel) // 2
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)
for a in range(offset, input_image.width - offset):
    for b in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for x in range(len(kernel)):
            for y in range(len(kernel)):
                an = a + x - offset
                bn = b + y - offset
                pixel = input_pixels[an, bn]
                acc[0] += pixel[0] * kernel[x][y]
                acc[1] += pixel[1] * kernel[x][y]
                acc[2] += pixel[2] * kernel[x][y]

        draw.point((a, b), (int(acc[0]), int(acc[1]), int(acc[2])))
output_image.show()
