#-----時間計測用-----#
from time import time
start_time = time()
#-----時間計測用-----#


#-----IMPORT-----#
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
#-----IMPORT-----#


#--------------Make(Set) Empty Graph--------------#
fig, ax = plt.subplots()
#--------------Make(Set) Empty Graph--------------#


#--------------Load Audio File--------------#
# wav_file_name = "audio\Conposition_Audio\out.wav"
wav_file_name = "audio\sample_Q_202205\sample_Q_202205\sample_Q_M01\sample_Q_M01\problem.wav"

n = librosa.get_samplerate(wav_file_name)

data, PCM = librosa.load(wav_file_name,sr = n)
print(len(data),PCM)
print(len(data)/PCM)
#--------------Load Audio File--------------#


#--------------Set Parameter--------------#
fft_size = 2048                 # Frame length
hl = int(fft_size / 4)          # Frame shift length
hi = 300                        # Height of image
wi = 300                        # Width of image
F_max = 20000                   # Freq max
window = np.blackman(fft_size)  # Window Function
#--------------Set Parameter--------------#


plt.rcParams["figure.figsize"] = [20, 10]
plt.rcParams["figure.autolayout"] = True
data = data[0:wi*hl]


#--------------STFT--------------#
S = librosa.feature.melspectrogram(
    y = data, sr = PCM, n_mels = hi, fmax = F_max, hop_length = hl, 
    win_length = fft_size, n_fft = fft_size, window = window)

S_dB = librosa.power_to_db(S, ref = np.max)
#--------------STFT--------------#


#--------------Data Plot--------------#
img = librosa.display.specshow(data = S_dB, x_axis = 'time', y_axis = 'mel',
                            sr = PCM, fmax = F_max, ax = ax, cmap = "gray")
#--------------Data Plot--------------#


#--------------Save Image--------------#
# plt.savefig("images/Mel_Spectrogram.png")
# plt.savefig("images/Japanese_01-20/Mel_Spectrogram_J01-20.png")
# plt.savefig("images/English_01-20/Mel_Spectrogram_E01-20.png")
plt.savefig("images/a.png")
# plt.show()
#--------------Save Image--------------#


#----------Read,Cut,SaveImage----------#
# Image Read
# img = cv2.imread("images/Mel_Spectrogram.png")

# img [top : bottom, left : right]
# img1 = img[58-1 : 428+1, 80-1: 577+1]
# cv2.imwrite("images/Mel_Spectrogram_cuted.png", img1)
#----------Read,Cut,SaveImage----------#


#-----時間計測用-----#
end_time = time()
print("Took",end_time - start_time,"seconds to run.")
#-----時間計測用-----#