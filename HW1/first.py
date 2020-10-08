import numpy as np
import math
import matplotlib.pyplot as plt

# Generate values for t
X = np.arange(-3, 3, 0.001)

# x1 function
Y = math.e ** (-3 * X)

plt.plot(X, Y, 'r.')
plt.show()

# x2 function
Y = (math.e ** (-3 * X)) * np.heaviside(X, 1)

plt.plot(X, Y, 'r.')
plt.show()

# x3 function
Y = (math.e ** (-3 * X)) * np.heaviside(X, 1) + (2 * np.sin(X + 2))

plt.plot(X, Y, 'r.')
plt.show()

# to find out x4 function we should split X to three parts
X_1 = X[X < -1]
X_2 = X[-1 <= X]
X_2 = X_2[X_2 <= 1]
X_3 = X[1 < X]

Y_1 = np.zeros(len(X_1))
Y_2 = np.ones(len(X_2))
Y_3 = math.e ** (-1 * X_3) * (np.sin(X_3) + np.cos(X_3)) * np.heaviside(X_3, 1)

plt.plot(X_1, Y_1, 'r.')
plt.plot(X_2, Y_2, 'r.')
plt.plot(X_3, Y_3, 'r.')
plt.show()
