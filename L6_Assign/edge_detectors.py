# source -https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html
# source - https://gist.github.com/rahit/c078cabc0a48f2570028bff397a9e154


import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    """
    This function takes no arguments as this reads the image and calculates the edges using laplace, sobel x and y.
    :return: none
    """
    img = cv2.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG", 0)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    plt.subplot(3, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    # laplace
    plt.subplot(3, 3, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    # sobel x
    plt.subplot(3, 3, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    # sobel y
    plt.subplot(3, 3, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    # prewitt
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv2.filter2D(img, -1, kernelx)
    img_prewitty = cv2.filter2D(img, -1, kernely)
    plt.subplot(3, 3, 5), plt.imshow(img_prewittx, cmap='gray')
    plt.title('prewitt x'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, 6), plt.imshow(img_prewitty, cmap='gray')
    plt.title('prewitt y'), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, 7), plt.imshow((img_prewittx + img_prewitty), cmap='gray')
    plt.title('prewitt x+y'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()
