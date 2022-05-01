from re import A
import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import wave
  
Accuracy = 100 # 粗さ。何フレーム毎にデータをとるか

# Load Audio File
wav_file_name = "./audio/asano_short.wav"
wav_file = wave.open(wav_file_name,"r")

PCM = wav_file.getframerate()   # PCM = Sampling = 48000
T_Frame = wav_file.getnframes() # Total_Frame ( = Sampling * Total_Time)
T_Time = T_Frame/PCM            # Total_Time ( = Total_Frame/PCM)

# 窓関数の定義
wav_file = wave.open(wav_file_name,"r")
data = wav_file.readframes(T_Frame)     # バイナリ読み込み
data = np.frombuffer(data,'int16')      # intに変換
# data = フレーム毎の振幅の大きさ
# 16bitの音声ファイルのデータを-32768 から 32767にプロット

print("PCM sampling :",PCM,"Hz")
print("Total Frame :",T_Frame,"Frames")
print("Total Time:Total Frame/Sampling")
print(" = ",T_Time,"sec")

size = 1024

hammingWindow = np.hamming(size)    # ハミング窓
d = 1 / PCM
freqList = np.fft.fftfreq(size, d)

windowedData = hammingWindow * data[:size]  # 切り出した波形データ（窓関数あり）
data = np.fft.fft(windowedData)

time = np.arange(0, T_Time, Accuracy/PCM)

plt.xlabel("Frequency[Hz]")
plt.ylabel("Loudness(bit)")

plt.plot(abs(freqList),abs(data))
plt.show()