# This is a sample Python script.
import pandas as pd
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def prep_1gb_data(a:int, p=None):
    rng = np.random.default_rng(seed=a)
    pp = rng.random((20000, 20000))
    return pp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dat = [prep_1gb_data(1)]

    for i in range(1, 250):
        a = int(input('Enter your input:'))
        if a > 0:
            dat.append(prep_1gb_data(a, dat[i - 1]))
        else:
            break
    rng = np.random.default_rng()
    n = 0
    for arr in dat:
        n = n+1
        rng.permuted(arr, axis=1, out=arr)
        print(n)
    input('Enter your input:')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
