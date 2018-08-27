import cv2 as cv


def return_smoothedimage(image, ksize):
    """
    This module gets the image and kernel size and returns the blurred image
    :param image: image matrix
    :param ksize: kernal size
    :return: blurred image
    """
    return cv.GaussianBlur(image, (ksize, ksize), 0)


def main():
    """
    this function gets the image and sends the image and kernel size data to return_smoothedimage function
    and gets the smoothed image
    :return: none
    """
    init_image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG", 0)
    cv.imshow("Smoothed image", return_smoothedimage(init_image, int(input("Enter the kernel size IN ODD ONLY!"))
                                                     ))
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
