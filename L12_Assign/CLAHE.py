# https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html


import cv2 as cv
import numpy as np


# noinspection PyUnresolvedReferences


def histogram_eq(img):
    equ = cv.equalizeHist(img)
    # res = np.hstack((img, equ))
    return equ


# noinspection PyUnresolvedReferences


def clahe_eq(img):
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    ret_img = clahe.apply(img)
    return ret_img


# noinspection PyUnresolvedReferences


def get_image():
    return cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\unequalized_image.jpg", 0)


# noinspection PyUnresolvedReferences


def main():
    const_img = get_image()
    hist_eq_img = histogram_eq(const_img)
    clahe = clahe_eq(const_img)
    # cv.imshow("histogram_eq <---> CLAHE", np.hstack((hist_eq_img, clahe)))
    cv.imshow("Original ", const_img)
    cv.imshow("Histogram equalised", hist_eq_img)
    cv.imshow("CLAHE equalised", clahe)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
