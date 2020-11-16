import numpy as np
import matplotlib.pyplot as plt


class Fourier:
    '''
    Fourier implements fourier transform for a single variable function.
    The function is given by the transform method and then you have transformed function in return.
    '''

    def __init__(self, c: int, T: int):
        self.c = c
        self.T = T

    def coefficients(self, x, y):
        '''
        Calculate fourier coefficient for given user function x and y.
        Please note that y is np.cos or np.sin.
        '''
        start = 0
        end = self.T
        step = 0.001
        t = np.arange(start, end, step)
        w0 = 2 * np.pi / self.T
        return np.vectorize(lambda k: np.sum(x(t) * y(t * k * w0)) * step * (2/self.T))(np.arange(0, self.c + 1))

    def ak(self, x):
        return self.coefficients(np.vectorize(x), np.cos)

    def bk(self, x):
        return self.coefficients(np.vectorize(x), np.sin)

    def transform(self, x):
        a = self.ak(x)
        b = self.bk(x)

        @np.vectorize
        def _transform(t):
            w0 = 2 * np.pi / self.T

            return np.sum(a * np.insert(np.cos(w0 * t * np.arange(1, a.size)), 0, 1/2)) \
                    + np.sum(b * np.insert(np.sin(w0 * t * np.arange(1, b.size)), 0, 0))

        return _transform



def right(input):
    '''
    Rigth is an example function based on homework question right example.
    '''
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
    '''
    Left is an example function based on homework question left example.
    '''
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

def plot(T, x):
    for c in range(15):
        ans = Fourier(c, T).transform(x)
        start = 0
        end = T
        step = 0.1
        t = np.arange(start, end, step)
        plt.scatter(t, ans(t))
        plt.show()


# plot(6, left)
plot(6, right)