# this file does basic 3D addition, multiplication, div, and subtraction
# this code uses numpy.random fill array values automatically
import numpy as np
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
        fir_arr = np.random.randint(255, size=(3, 3, 3))
        sec_arr = np.random.randint(255, size=(3, 3, 3))
        print("FIRST RANDOM ARRAY")
        print(fir_arr)
        print("SECOND RANDOM ARRAY")
        print(sec_arr)
        result = do_something(fir_arr, sec_arr)
        result = np.clip(result, None, 255)
        print("RESULT")
        print(result)
        plt.imshow(result, interpolation="none")
        plt.show()
except KeyboardInterrupt:
    print("USER EXITED")
