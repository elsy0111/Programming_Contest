import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import cv2

fig, ax = plt.subplots()

# Load Audio File
wav_file_name = "audio/Sample_Audio/asano_short30-35.wav"
data, PCM = librosa.load(wav_file_name)

fft_size = 2048                 # Frame length
hl = int(fft_size / 4)          # Frame shift length
hi = 512                        # Height of image
wi = 256                        # Width of image
F_max = 10000                   # Freq max
window = np.blackman(fft_size)  # Window Function

plt.rcParams["figure.figsize"] = [20, 10]
plt.rcParams["figure.autolayout"] = True
data = data[0:wi*hl]

S = librosa.feature.melspectrogram(
    y = data, sr = PCM, n_mels = hi, fmax = F_max, hop_length = hl, 
    win_length = fft_size, n_fft = fft_size, window = window)

S_dB = librosa.power_to_db(S, ref = np.max)

# Data Plot
img = librosa.display.specshow(data = S_dB, x_axis = 'time', y_axis = 'mel',
                            sr = PCM, fmax = F_max, ax = ax, cmap = "gray")

# Save Image
plt.savefig("images/Mel_Spectrogram_nd.png")
# plt.show()

# Image Read
img = cv2.imread("images/Mel_Spectrogram_nd.png")

# img [top : bottom, left : right]
# Cut,Save Image
img1 = img[58-1 : 428+1, 80-1: 577+1]
cv2.imwrite("images/Mel_Spectrogram_nd_cuted.png", img1)