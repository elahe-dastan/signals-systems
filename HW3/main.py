import numpy as np
import array as arr
import matplotlib.pyplot as plt


def coefficient(T, x, y, c):
    start = 0
    end = T
    step = 0.001
    t = np.arange(start, end, step)
    ans = arr.array('d', [])
    w0 = 2 * np.pi / T
    for k in range(0, c + 1):
        integral = 0
        for i in t:
            partial = x(i) * y(k * w0 * i)
            integral += partial * step
        ans.append((2 / T) * integral)
    return ans


def ak(T, x, c):
    return coefficient(T, x, np.cos, c)


def bk(T, x, c):
    return coefficient(T, x, np.sin, c)


def right(input):
    T = 6
    while input > 3:
        input = input - T

    while input < -3:
        input = input + T

    if input == 3 or input == 0 or input == -3:
        return 0
    if 0 < input < 3:
        return -1
    if -3 < input < 0:
        return 1


def left(input):
    T = 6
    while input > 3:
        input = input - T

    while input < -3:
        input = input + T

    if (-3 <= input <= -2) or (2 <= input <= 3):
        return 0

    if -2 < input <= -1:
        return input + 2

    if 1 <= input < 2:
        return input - 2

    if -1 < input < 1:
        return -1 * input

def signal(a, b, T, t):
    sum = 0
    sum += a[0] / 2
    w0 = 2 * np.pi / T
    for k in range(1, len(a)):
        sum += a[k] * np.cos(k * w0 * t)
        sum += b[k] * np.sin(k * w0 * t)
    return sum


def plot(T, x):
    for c in range(15):
        a = ak(T, x, c)
        b = bk(T, x, c)
        start = 0
        end = T
        step = 0.1
        t = np.arange(start, end, step)
        ans = arr.array('d', [])
        for i in t:
            ans.append(signal(a, b, T, i))
        plt.scatter(t, ans)
        plt.show()


plot(6, left)

# start = 0
# end = 6
# step = 0.1
# t = np.arange(start, end, step)
# ans = arr.array('d', [])
# for i in t:
#     ans.append(left(i))
# plt.scatter(t, ans)
# plt.show()
