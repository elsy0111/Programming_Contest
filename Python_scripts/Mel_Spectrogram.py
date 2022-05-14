import scipy.io.wavfile
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import wave


fft_size = 2048                  # フレーム長            
hop_length = int(fft_size / 4)   # フレームシフト長 

# Load Audio File
wav_file_name = "audio/Sample_Audio/asano_short30-35.wav"
wav_file = wave.open(wav_file_name,"r")

PCM, data = scipy.io.wavfile.read(wav_file_name)    # PCM = Sampling = 48000
T_Frame = wav_file.getnframes()                     # Total_Frame ( = Sampling * Total_Time)
T_Time = T_Frame/PCM                                # Total_Time ( = Total_Frame/PCM)

# Down Sampling
data = data[::2]
PCM = PCM/2

# Print Meta Data
print("PCM sampling :",PCM,"Hz")
print("Total Frame :",len(data),"Frames")
print("Total Time:Total Frame/Sampling",end = "")
print(" = ",T_Time,"sec")

# 16bitの音声ファイルのデータを-1から1に正規化
data = data / 32768

# 窓関数,解像度?を設定
window = "hann"
n_mels = 512
mel_power = librosa.feature.melspectrogram(
    y = data, n_fft = fft_size, hop_length = hop_length, win_length = fft_size,
    window = window, n_mels = n_mels)
mel_power_in_db = librosa.power_to_db(mel_power, ref=np.max)

# Data Plot
librosa.display.specshow(mel_power_in_db,x_axis='time', y_axis='mel', sr=PCM,cmap = "gray")
# plt.colorbar(format='%+2.0f dB')

plt.savefig("images/Mel_Spectrogram_d.png",dpi = 600)  # プロットしたグラフをファイルsave.pngに保存する
plt.show()