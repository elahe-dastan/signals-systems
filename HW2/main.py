import numpy as np
import math
import matplotlib.pyplot as plt


# The first part of the question
def convolve(a, b):
    n = len(a) + len(b) - 1

    if len(a) > len(b):
        a, b = b, a

    k = len(a)

    ans = []
    for i in range(n):
        sum = 0
        for j in range(k):
            if 0 <= i - j < len(b):
                sum += a[j] * b[i - j]
        ans.append(sum)

    return ans


t = np.arange(-10, 10, 0.1)

x = []
for i in t:
    x.append(1 / 2 * math.exp(-2 * i) * np.heaviside(i, 1))

h = np.heaviside(t, 1) - np.heaviside(t - 5, 1)

plt.plot(convolve(x, h))
plt.show()



