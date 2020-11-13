import numpy as np
import array as arr


def ak(T, x, c):
    start = 0
    end = T
    step = 0.001
    t = np.arange(start, end, step)
    ans = arr.array('d', [])
    for k in range(1, c+1):
        w0 = 2 * np.pi / T
        partial = x(t) * np.cos(k * w0 * t)
        integral = np.sum(partial) * step
        ans.append((2 / T) * integral)
    return ans

def x(input):
    return input**2

print(ak(2,x,1))

