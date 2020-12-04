from scipy.io import wavfile
from scipy.fftpack import fft, ifft, fftfreq
import numpy as np
from matplotlib import pyplot as plt
import wave

HIDDEN_CODE_START_INDEX = 300000

# get the file sample rate and data
s_rate, signal = wavfile.read('samples/sample_1.wav')
# w = wave.open('samples/sample_1.wav', "rb")
# binary_data = w.readframes(w.getnframes())
# w.close()

# print(binary_data)

# fast fourier transform
FFT = abs(fft(signal))

# define frequency vector
freqs = fftfreq(len(FFT)) * s_rate

# freq_no_idea = np.array([])
# signal_no_idea = np.array([])
#
# for i in range(len(freqs)):
#     if cut_freq_signal[i] != 0:
#         np.append(freq_no_idea, freq_no_idea[i])
#         np.append(signal_no_idea, signal_no_idea[i])

# for f in freqs:
#     print(f)
# make non code frequency zero
# FFT_code_range = np.append(np.zeros(300000), FFT[range(HIDDEN_CODE_START_FREQUENCY, len(FFT) // 2)])
# print(len(FFT) // 2)
# print(len(FFT_code_range))

# # FFT_code_range = FFT[range(HIDDEN_CODE_START_FREQUENCY, len(FFT) // 2)]
# # freqs_code_range = freqs[range(HIDDEN_CODE_START_FREQUENCY, len(FFT) // 2)]
#
# plot
plt.plot(freqs, cut_freq_signal)
# plt.xlim([300000, len(FFT) // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()
