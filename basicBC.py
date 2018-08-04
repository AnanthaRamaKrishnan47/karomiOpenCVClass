# this file contains code to control brightness and contrast of an image
# by doing simple point operations (i.e addition or multiplication)
# http://cartucho.github.io/tutorial_basic_linear_transform.html
import numpy as np
import cv2 as cv

contrast = float(input("Enter the contrast amount value should be around 1.0-3.0"))
brightness = int(input("Enter the brightness amount value should be around 1 - 100"))

monkey_Image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")

modC_Img = cv.multiply(monkey_Image, np.array([contrast]))
modB_Img = cv.add(modC_Img, brightness)

cv.imshow("Original", monkey_Image)
cv.imshow("Modified contrast and brightness", modB_Img)

cv.waitKey(0)
cv.destroyAllWindows()