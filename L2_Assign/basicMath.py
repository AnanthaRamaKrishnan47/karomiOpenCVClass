# this file does basic 3D addition, multiplication, div, and subtraction
# this code uses numpy.random fill array values automatically
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def do_something(arr_1, arr_2):
    print("Enter 1 fot Addition")
    print("Enter 2 fot Subtraction")
    print("Enter 3 fot Multiplication")
    print("Enter 4 fot Division")

    case = int(input("Enter what operation you're going to do!"))

    return {
        1: (arr_1+arr_2),
        2: (arr_1-arr_2),
        3: (arr_1*arr_2),
        4: (arr_1/arr_2),
    }.get(case, "ERROR")


try:
    while True:
        image = cv.imread(r"C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\mandarin_monkey.PNG")
        w, h, d = image.shape
        fir_arr = np.random.randint(1024, size=(5, 5, 3))
        sec_arr = np.random.randint(1024, size=(5, 5, 3))
        print("FIRST RANDOM ARRAY")
        print(fir_arr)
        print("SECOND RANDOM ARRAY")
        print(sec_arr)
        result = do_something(fir_arr, sec_arr)
        print(result)
        result[np.where(result > 255)] = (result[np.where(result > 255)] % 255) - 1
        # Methods that didi not work
        # result = np.clip(result, None, 255)
        # result = np.putmask(result, result > 255, result/4)
        # result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
        # result = np.dot(result, [0.299, 0.587, 0.114])
        # result = cv.normalize(result, 0, 255)
        print("RESULT")
        print(result)
        plt.imshow(result, interpolation="none")
        plt.show()
except KeyboardInterrupt:
    print("USER EXITED")
