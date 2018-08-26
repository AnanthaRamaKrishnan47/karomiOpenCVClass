# source - https://github.com/fubel/PyCannyEdge

import scipy as simage
import numpy as np
import cv2 as cv


image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG",
                  cv.IMREAD_GRAYSCALE)
cv.imshow("Is it grey?", image)
cv.waitKey(0)
cv.destroyAllWindows()
h_kernel = np.array([[0, 0, 0], [0, -1, 1], [0, 0, 0]])
print(image.shape)
print(h_kernel.shape)
out = simage.convolve(image, h_kernel)
cv.imshow("Convolved image", out)
