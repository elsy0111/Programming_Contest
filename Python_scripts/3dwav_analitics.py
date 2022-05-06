from re import A
import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import wave
 
Accuracy = 100 # 粗さ 何フレーム毎にデータをとるか

# Load Audio File
wav_file_name = "./audio/Sample_Audio/asano_short.wav"
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

# Print Meta Data
print("PCM sampling :",PCM,"Hz")
print("Total Frame :",T_Frame,"Frames")
print("Total Time:Total Frame/Sampling")
print(" = ",T_Time,"sec")

# np.arange(初項 = 初めの時間[sec], 
#           等差数列の終点　= 終わりの時間[sec], 
#           等差[sec])

time = np.arange(0, T_Time, Accuracy/PCM)

size = 2400

hammingWindow = np.hamming(size)    # ハミング窓
d = 1 / PCM
freq = np.fft.fftfreq(size, d)

windowedData = hammingWindow * data[:size]  # 切り出した波形データ（窓関数あり）
data = np.fft.fft(windowedData)

# Setting Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Set Graph Title , Axis Label
ax.set_title("wav_3d",size=20)
ax.set_xlabel("Time[s]",size=15,color="black")
ax.set_ylabel("Loudness(bit)",size=15,color="black")
ax.set_zlabel("Frequency[Hz]",size=15,color="black")

# # Down Sampling
# data = data
# freq = freq

# Setting x,y,z
x = time
y = abs(freq)
z = abs(data)

print(len(time))
print(len(data))
print(len(freq))

# Data Plot
ax.scatter(x,y,z)
plt.show()