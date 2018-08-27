# source - https://github.com/fubel/PyCannyEdge
# source - http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html
# source - https://www.packtpub.com/mapt/book/application_development/9781785283932/2/ch02lvl1sec21/motion-blur


import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from skimage import io, color
# from skimage import exposure


def return_kernel(case):
    """
    This function returns the kernel based on the angle given only in 0,45,90,125
    :param case: given angle
    :return: angled kernel
    """
    return {
        0: (np.array([[0, 0, 0], [0, -1, 1], [0, 0, 0]])),
        90: (np.array([[0, 1, 0], [0, -1, 0], [0, 0, 0]])),
        45: (np.array([[0, 0, 1], [0, -1, 0], [0, 0, 0]])),
        125: (np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])),
    }.get(case, "ERROR")


def main():
    """
    This is the main function that loads the image, gets kernel based on angle, performs calculation(convolution)
    and lets us view the edges
    :return:
    """
    # Load the image
    img = io.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
    img = color.rgb2gray(img)  # Convert the image to grayscale (1 channel)
    kernel = return_kernel(int(input("Enter what operation you're going to do!")))
    # we use 'valid' which means we do not add zero padding to our image
    edges = scipy.signal.convolve2d(img, kernel, 'valid')
    plt.imshow(edges, cmap=plt.cm.gray)  # plot the edges_clipped
    # plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
