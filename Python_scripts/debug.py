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

time = np.arange(0, T_Time, 1/PCM)

plt.plot(time, data)
plt.show()