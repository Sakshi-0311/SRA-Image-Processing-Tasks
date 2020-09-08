from PIL import Image
import numpy as np
import math


def roundoff(number):
    temp = int(number)
    if number > temp:
        return round(temp + 1)
    else:
        return round(temp)


def rot(image, angle):
    angle = math.radians(angle)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    new_width = roundoff(abs(image.shape[0] * cosine) + abs(image.shape[1] * sine))
    new_height = roundoff(abs(image.shape[1] * cosine) + abs(image.shape[0] * sine))

    image1 = np.zeros((roundoff(new_width), roundoff(new_height), image.shape[2]))
    centre_row = round(((image.shape[0] + 1) / 2) - 1)
    centre_column = round(((image.shape[1] + 1) / 2) - 1)

    centre_height = round(((new_height + 1) / 2) - 1)
    centre_width = round(((new_width + 1) / 2) - 1)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            y = image.shape[0] - 1 - i - centre_row
            x = image.shape[1] - 1 - j - centre_column
            X = round(x * cosine + y * sine)
            Y = round(-x * sine + y * cosine)
            X = centre_height - X
            Y = centre_width - Y

            if image1.shape[1] > X >= 0 and image1.shape[0] > Y >= 0:
                image1[Y, X, :] = image[i, j, :]
    for i in range(image1.shape[0]):
        prev = [image1[i][0][0], image1[i][0][1], image1[i][0][2], image1[i][0][3]]
        for j in range(image1.shape[1] - 1):
            if not any(image1[i][j][:]):
                if any(image1[i][j + 1][:]):
                    image1[i][j][:] = prev
            else:
                prev = image1[i][j][:]
    return image1


im = np.array(Image.open('rotate.png'))
rotation_angle = int(input("Enter the angle: "))
im_copy = rot(im, rotation_angle)
rotate = Image.fromarray(im_copy.astype(np.uint8))
rotate.save("Rotated-Image.png")
rotate.show()
