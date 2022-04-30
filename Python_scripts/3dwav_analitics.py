import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
 
#音声ファイル読み込み
wav_filename = "./audio/asano_short.wav"
PCM, data = scipy.io.wavfile.read(wav_filename)

#縦軸（振幅）の配列 = data   
# 16bitの音声ファイルのデータは-32768から32767の2^16(65,536)段階
#PCM(Sampling = 48000)
T_Flame = data.shape[0] #Total_Flame( = Sampling * Total_Time)
T_Time = T_Flame/PCM #Total_Time( = Total_Flame/PCM)

print("PCM sampling :",PCM,"Hz")
print("Total Flame :",T_Flame,"Flames")
print("Total Time:Total Flame/Sampling")
print(" = ",T_Time,"sec")

##### 音声データをそのまま表示する #####

#横軸（時間）の配列 = time
##np.arange(初項 = 初めの時間[sec], 
#           等差数列の終点　= 終わりの時間[sec], 
#           等差[sec])
time = np.arange(0, T_Time, 100/PCM)
print(len(data))

freq = np.fft.fftfreq(T_Flame, d=100/PCM)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#グラフタイトル,軸名を設定
ax.set_title("wav_3d",size=20)
ax.set_xlabel("Time[s]",size=15,color="black")
ax.set_ylabel("Loudness(bit)",size=15,color="black")
ax.set_zlabel("Frequency",size=15,color="black")

data = data[::100]
print(48000*5)

freq = freq[::100]

x = time
y = data
z = freq

print(len(data))
print(48000*5/4)

print(len(time))
print(len(freq))

#データプロット
ax.scatter(x,y,z)
plt.show()