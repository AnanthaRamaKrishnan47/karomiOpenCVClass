import cv2 as cv
import numpy as np,sys


# noinspection PyUnresolvedReferences


def get_image():
    return cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")


def get_iteration_limit(length):
    ret_limit = 0
    len_mod = length

    while len_mod > 1:
        len_mod /= 2
        ret_limit += 1
    return ret_limit


# noinspection PyUnresolvedReferences


def main():
    m_monkey = get_image()
    print("Original size: ", m_monkey.shape)
    gaussian_py = m_monkey.copy()
    gpA = [gaussian_py]
    iteration_limit = get_iteration_limit(gaussian_py.shape[0])
    for i in range(iteration_limit):
        gaussian_py = cv.pyrDown(gaussian_py)
        cv.imshow("Gaussian py", gaussian_py)
        cv.waitKey(0)
        cv.destroyAllWindows()

    # gpA.append(gaussian_py)
    # cv.imshow("Gaussian py", gpA)


if __name__ == '__main__':
    main()
