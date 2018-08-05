# import openCV
import cv2
import numpy as np
image = cv2.imread(r"C:\Users\krishnan\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
b, g, r = cv2.split(image)
# declaring an variable of same dimension as image
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red filter", r)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imshow("Blue filter", b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imshow("Green filter", g)
cv2.imshow("Red channel", cv2.merge([zeros, zeros, r]))
cv2.imshow("Blue channel", cv2.merge([b, zeros, zeros]))
cv2.imshow("Green channel", cv2.merge([zeros, g, zeros]))
cv2.imwrite(r"C:\Users\krishnan\PycharmProjects\KaromiOpenCvClass\sample images\redFil.jpeg",
            cv2.merge([zeros, zeros, r]))
cv2.imwrite(r"C:\Users\krishnan\PycharmProjects\KaromiOpenCvClass\sample images\blueFil.jpeg",
            cv2.merge([b, zeros, zeros]))
cv2.imwrite(r"C:\Users\krishnan\PycharmProjects\KaromiOpenCvClass\sample images\greenFil.jpeg",
            cv2.merge([zeros, g, zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()


