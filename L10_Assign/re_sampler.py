# https://medium.com/@manivannan_data/resize-image-using-opencv-python-d2cdbbc480f0
# http://www.xinapse.com/Manual/interpolation.html
# https://upload.wikimedia.org/wikipedia/commons/9/90/Comparison_of_1D_and_2D_interpolation.svg
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
import cv2 as cv
import numpy as np


def get_sample_rate():
    print("Enter number range between 1 - 2. (1-.9) for desampling - (1.1 - 2.0) for upsampling ")
    ret_sample_rate = float(input("Enter between 0-2"))
    return ret_sample_rate

# noinspection PyUnresolvedReferences


def mse(imagea, imageb):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imagea.astype("float") - imageb.astype("float")) ** 2)
    err /= float(imagea.shape[0] * imagea.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


# noinspection PyUnresolvedReferences


def main():
    sample_rate = get_sample_rate()
    image_const = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG", 0)
    # print(image_const.shape)
    # dst = image_const.copy()
    # print(dst.shape)
    dst = cv.resize(image_const, None, fx=sample_rate, fy=sample_rate, interpolation=cv.INTER_NEAREST)
    dst_2 = cv.resize(dst, None, fx=2, fy=2, interpolation=cv.INTER_NEAREST)
    dst_3 = cv.resize(dst, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
    cv.imshow("Downsampled image", dst)
    cv.imshow("Upsampled image_NEAREST", dst_2)
    cv.imshow("Upsampled image_CUBIC", dst_3)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("MSE between original & downAndUpsampled bi-cubic image is: ", mse(image_const, dst_3))
    print("MSE between original & downAndUpsampled Nearest neighbour image is: ", mse(image_const, dst_2))


if __name__ == '__main__':
    main()
