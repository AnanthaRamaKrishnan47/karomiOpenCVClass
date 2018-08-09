# import numpy and openCV lib
import cv2 as cv
import numpy as np


image = cv.imread(r"C:\Users\krishnan\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
# row, col, ch = image.shape
# mean = 0
# var = 100
# sigma = var*.5
# gauss = np.random.normal(mean, sigma, (row, col, ch))
# gauss = gauss.reshape(row, col, ch)
# gauss = np.random.randint(0, 25, image.shape, dtype="uint8")
print(image.shape)
# np.random.normal param 1 - mean, param 2 - variance, param 3 - image shape (or) size
gauss = np.random.normal(1, 100, image.shape)
print(gauss)
cv.imshow("gauss noise", gauss)
noisy = image + gauss
cv.imshow("Noiseless image", image)
cv.imshow("Noise introduced image", noisy)
cv.waitKey(0)
cv.destroyAllWindows()
