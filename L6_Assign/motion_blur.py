import numpy as np
import cv2 as cv


def return_h_motion_blur():
    return np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])


def return_v_motion_blur():
    return np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])


def return_kernel(size):
    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size
    return kernel_motion_blur


def main():
    image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG", 0)
    # output_h = cv.filter2D(image, -1, return_h_motion_blur())
    output_v = cv.filter2D(image, -1, int(input("Enter the kernel size !")))
    # cv.imshow("Horizondal motion blur", output_h)
    cv.imshow("Vertical  motion blur", output_v)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
