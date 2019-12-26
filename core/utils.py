import numpy as np


def rotate(matrix, *args):
    return np.rot90(matrix, -1)


def mirror(matrix, *args):
    return np.flip(matrix, 1)


def inverse(matrix, *args):
    return 255 - matrix


def bw(matrix, *args):
    r, g, b = matrix[:,:,0], matrix[:,:,1], matrix[:,:,2]
    return 0.299 * r + 0.587 * g + 0.114 * b


def sharpen(matrix, *args):
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])
    return apply_filter(matrix, sharpening_kernel)


def lighten(matrix, *args):
    percentage = args[0] / 100
    f = lambda x: min(255, x + x * percentage)
    vf = np.vectorize(f)
    return vf(matrix)


def darken(matrix, *args):
    percentage = args[0] / 100
    f = lambda x: x - x * percentage
    vf = np.vectorize(f)
    return vf(matrix)


def apply_on_rgb(image, kernel):
    imgOut = np.zeros(image.shape, dtype=np.uint8)

    ks = kernel.shape[1]
    padding = ks // 2

    image = np.pad(image, ((padding, padding), (padding, padding), (0, 0)), 'constant', constant_values=(0))
    for row in range(padding, image.shape[0] - padding):
        for col in range(padding, image.shape[1] - padding):
            value = image[(row - padding):(row + padding + 1), (col - padding):(col + padding + 1)]
            R = value[0:ks, 0:ks, 0]
            G = value[0:ks, 0:ks, 1]
            B = value[0:ks, 0:ks, 2]
            pixel = [min(255, max(0, (R * kernel).sum())),
                     min(255, max(0, (G * kernel).sum())),
                     min(255, max(0, (B * kernel).sum()))
                     ]
            imgOut[row-padding, col-padding] = pixel
    return imgOut


def apply_on_grayscale(image, kernel):
    imgOut = np.zeros(image.shape, dtype=np.uint8)

    ks = kernel.shape[1]
    padding = ks // 2

    image = np.pad(image, ((padding, padding), (padding, padding)), 'constant', constant_values=(0))
    for row in range(padding, image.shape[0] - padding):
        for col in range(padding, image.shape[1] - padding):
            value = image[(row - padding):(row + padding + 1), (col - padding):(col + padding + 1)]
            pixel = min(255, max(0, (value * kernel).sum()))
            imgOut[row - padding, col - padding] = pixel
    return imgOut


def apply_filter(image: np.array, kernel: np.array) -> np.array:
    assert image.ndim in [2, 3]
    assert kernel.ndim == 2
    assert kernel.shape[0] == kernel.shape[1]

    if image.ndim == 3:
        return apply_on_rgb(image, kernel)
    elif image.ndim == 2:
        return apply_on_grayscale(image, kernel)