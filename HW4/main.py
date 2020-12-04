from scipy.io import wavfile
from scipy.fft import fft
from scipy import fftpack
import numpy as np
from matplotlib import pyplot as plt

# get the file sample rate and data
s_rate, signal = wavfile.read('samples/sample_1.wav')

# fast fourier transform
FFT = abs(fft(signal))

# define frequency vector
freqs = fftpack.fftfreq(len(FFT), 1/s_rate)

# plot
plt.plot(freqs, FFT)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()
