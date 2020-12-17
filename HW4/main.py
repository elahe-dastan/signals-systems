from scipy.io import wavfile
from scipy.fftpack import fft
from matplotlib import pyplot as plt
import matplotlib as mpl
import sys

HIDDEN_CODE_START_INDEX = 300000

# get the file sample rate and data
s_rate, signal = wavfile.read('samples/' + sys.argv[1])

# fast fourier transform
FFT = fft(signal)
FFT_code = FFT[HIDDEN_CODE_START_INDEX:]
# plt.axis([0, 80, -1e6, 1e6])
# plt.plot(FFT_code)
# plt.show()
# mpl.use('Qt5Agg')

code_bytes = []
decimal = 0
position = 128
for i in range(0, 650, 10):
    if i % 80 == 0 and i != 0:
        code_bytes.append(chr(int(decimal)))
        decimal = 0
        position = 128
    if FFT_code[i] > 0:
        decimal += position
    position /= 2


print(code_bytes)
