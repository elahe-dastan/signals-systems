from scipy.io import wavfile
import scipy
from scipy import fftpack
import numpy as np
from matplotlib import pyplot

# get the file sample rate and data
s_rate, signal = wavfile.read('samples/sample_1.wav')
print(s_rate, signal)
