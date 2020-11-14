import numpy as np
import array as arr


def coefficient(T, x, y, c):
    start = 0
    end = T
    step = 0.001
    t = np.arange(start, end, step)
    ans = arr.array('d', [])
    for k in range(1, c + 1):
        w0 = 2 * np.pi / T
        partial = x(t) * y(k * w0 * t)
        integral = np.sum(partial) * step
        ans.append((2 / T) * integral)
    return ans


def ak(T, x, c):
    return coefficient(T, x, np.cos, c)


def bk(T, x, c):
    return coefficient(T, x, np.sin, c)


def x(input):
    return input ** 2


print(bk(2, x, 1))
