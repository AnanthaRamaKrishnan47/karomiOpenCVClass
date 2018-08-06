# import numpy and openCV lib
import cv2 as cv
import numpy as np


image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
row, col, ch = image.shape
mean = 0
var = 100
sigma = var*.5
gauss = np.random.normal(mean, sigma, (row, col, ch))
gauss = gauss.reshape(row, col, ch)
noisy = image + gauss
cv.imshow("Noiseless image", image)
cv.imshow("Noise introduced image", noisy)
cv.waitKey(0)
cv.destroyAllWindows()
