from PIL import Image
import numpy as np


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def convolve3d_grayscale(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1))
    image_padded[kernel.shape[0] - 2:-1:, kernel.shape[1] - 2:-1:] = image
    image_padded[0, 0] = image[0, 0]
    image_padded[-1, -1] = image[-1, -1]
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y, x] = (kernel * image_padded[y: y + kernel.shape[0], x: x + kernel.shape[1]]).sum()
    return output


gauss = np.array([[1, 4, 6, 4, 1],
                           [4, 16, 24, 16, 4],
                           [6, 24, 36, 24, 6],
                           [4, 16, 24, 16, 4],
                           [1, 4, 6, 4, 1]]) / 256

x_direction_kernel = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])

y_direction_kernel = np.array([[-1, -2, -1],
                               [0, 0, 0],
                               [1, 2, 1]])

img = "edge-detection2.jpg"
im = rgb2gray(np.array(Image.open(img)))
im = convolve3d_grayscale(im, gauss)
im_x = convolve3d_grayscale(im, x_direction_kernel)
im_y = convolve3d_grayscale(im, y_direction_kernel)
im = np.hypot(im_x, im_y)
sobel = Image.fromarray(im).convert('RGB')
sobel.show()
sobel.save('Sobel Edge Detection-Cube.jpg')
