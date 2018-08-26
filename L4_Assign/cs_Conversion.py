# doubt - https://www.mathworks.com/matlabcentral/answers/231932-is-this-how-to-calculate-mean-square
# -error-for-two-images


import numpy as np
import cv2 as cv


def bgr2_ycrcb(image):

    """
    This function takes the primary image as input and converts it into ycrcb format and lets us view it!
    after converting it  to the above mentioned format, then i convert it into BGR to calculate the mean error.
    The mean error is printed in console.
    :param image: Primary image input that is converted to ycrcb -> bgr and calculated RMS
    :return: NONE
    """

    image_ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    image_restore = cv.cvtColor(image_ycrcb, cv.COLOR_YCrCb2BGR)
    error = (image - image_restore)
    rms = np.sqrt(np.mean(error ** 2))
    print(rms)
    cv.imshow("BGR2YCRCB", image_ycrcb)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
    bgr2_ycrcb(image)


if __name__ == '__main__':
    main()
