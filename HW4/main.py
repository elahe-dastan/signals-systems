from scipy.io import wavfile
from scipy.fftpack import fft, ifft, fftfreq
from matplotlib import pyplot as plt
import wave

HIDDEN_CODE_START_INDEX = 300000

# get the file sample rate and data
s_rate, signal = wavfile.read('samples/sample_1.wav')

# fast fourier transform
FFT = abs(fft(signal))

# define frequency vector
freqs = fftfreq(len(FFT)) * s_rate

# make non code frequency zero
FFT_code_range = FFT[range(HIDDEN_CODE_START_INDEX, len(FFT) // 2)]

# # FFT_code_range = FFT[range(HIDDEN_CODE_START_FREQUENCY, len(FFT) // 2)]
# # freqs_code_range = freqs[range(HIDDEN_CODE_START_FREQUENCY, len(FFT) // 2)]

IFFT = ifft(FFT_code_range)


codeInBytes = IFFT.tobytes()[0:8]
print(codeInBytes)
print(type(codeInBytes))
for b in codeInBytes:
    print(type(b))
    print(int.from_bytes(b, byteorder="big"))

# plt.plot(IFFT)
# plt.show()
# plot
# plt.plot(freqs[range(len(FFT) // 2)], FFT_code_range)
# # plt.xlim([300000, len(FFT) // 2])
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.show()
