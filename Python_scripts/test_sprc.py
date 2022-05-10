import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

wav_file_name = "audio/Sample_Audio/asano_short.wav"
sample_rate, samples = wavfile.read(wav_file_name)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()