import scipy.io.wavfile
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import wave


fft_size = 2048                  # フレーム長            
hop_length = int(fft_size / 16)  # フレームシフト長 

# Load Audio File
wav_file_name = "audio/Sample_Audio/asano_short20-25.wav"
wav_file = wave.open(wav_file_name,"r")

PCM, data = scipy.io.wavfile.read(wav_file_name)    # PCM = Sampling = 48000
T_Frame = wav_file.getnframes()                     # Total_Frame ( = Sampling * Total_Time)
T_Time = T_Frame/PCM                                # Total_Time ( = Total_Frame/PCM)


# Print Meta Data
print("PCM sampling :",PCM,"Hz")
print("Total Frame :",T_Frame,"Frames")
print("Total Time:Total Frame/Sampling",end = "")
print(" = ",T_Time,"sec")


# np.arange(初項 = 初めの時間[sec], 
#           等差数列の終点　= 終わりの時間[sec], 
#           等差[sec])
time = np.arange(0, T_Time, 1/PCM)


#16bitの音声ファイルのデータを-1から1に正規化
data = data / 32768


# 短時間フーリエ変換実行
amplitude = np.abs(librosa.core.stft(data, n_fft=fft_size, hop_length=hop_length))
# 振幅をデシベル単位に変換
log_power = librosa.core.amplitude_to_db(amplitude)

# Data Plot
librosa.display.specshow(
    log_power, sr = PCM, hop_length = hop_length,
    x_axis="time", y_axis="hz", cmap='magma')
plt.colorbar(format='%+2.0f dB')

plt.savefig("images/save.png", dpi = 800)  # プロットしたグラフをファイルsave.pngに保存する
plt.show()