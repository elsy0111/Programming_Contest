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
PCM, data = scipy.io.wavfile.read(wav_file_name)

# data = 16bitの音量 、1Frameあたり１つのデータ
#  ( = len(data) = Total_Frame)  
# 16bitの音声ファイルのデータは-32768から32767の2^16(65,536)段階を
# 0~32767に変換
data = abs(data)
# PCM( = Sampling = 48000)
T_Frame = data.shape[0] # Total_Frame( = Sampling * Total_Time)
T_Time = T_Frame/PCM    # Total_Time( = Total_Frame/PCM)

# 窓関数の定義
wav_file = wave.open(wav_file_name,"r")
amp  = (2**8) ** wav_file.getsampwidth() / 2
data = wav_file.readframes(T_Frame)     # バイナリ読み込み
data = np.frombuffer(data,'int16')      # intに変換
data = data / amp                       # 振幅正規化