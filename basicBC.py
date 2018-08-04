# this file contains code to control brightness and contrast of an image
# by doing simple point operations (i.e addition or multiplication)

import numpy as np
import cv2 as openCv

contrast = float(input("Enter the contrast amount value should be around 1.0-3.0"))
brightness = int(input("Enter the brightness amount value should be around 1 - 100"))

monkey_Image = openCv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")

modC_Img = openCv.multiply(monkey_Image, np.array([contrast]))
modB_Img = openCv.add(modC_Img, brightness)

openCv.imshow("Original", monkey_Image)
openCv.imshow("Modified contrast and brightness", modB_Img)

openCv.waitKey(0)
openCv.destroyAllWindows()