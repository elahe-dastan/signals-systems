import numpy as np
import matplotlib.pyplot as plt

# Generate values for n
X = np.arange(-20, 20, 1)

# # x1 function
# Y = np.heaviside(X, 1) - np.heaviside(X - 3, 1) + np.heaviside(X - 5, 1)
#
# plt.plot(X, Y, 'ro')
# plt.show()

# x2 function
# k = 1
# Y = 2 * np.cos(2 * np.pi * X)
#
# plt.plot(X, Y, 'ro')
# plt.show()
#
# # k = 2
# Y = 2 * np.cos(2 * np.pi * 2 * X)
#
# plt.plot(X, Y, 'ro')
# plt.show()
#
# # k = 3
# Y = 2 * np.cos(2 * np.pi * 3 * X)
#
# plt.plot(X, Y, 'ro')
# plt.show()

# x3 function
# k = 1
Y = 2 * np.cos(2 * X)

plt.plot(X, Y, 'ro')
plt.show()

# k = 2
Y = 2 * np.cos(2 * 2 * X)

plt.plot(X, Y, 'ro')
plt.show()

# k = 3
Y = 2 * np.cos(2 * 3 * X)

plt.plot(X, Y, 'ro')
plt.show()


