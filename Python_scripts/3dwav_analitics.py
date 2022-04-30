import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
Accuracy = 100 #粗さ。何フレーム毎にデータをとるか

#Load Audio File
wav_filename = "./audio/asano_short.wav"
PCM, data = scipy.io.wavfile.read(wav_filename)

#data = 16bitの音量 、1Flameあたり１つのデータ
#  ( = len(data) = Total_Flame)  
# 16bitの音声ファイルのデータは-32768から32767の2^16(65,536)段階を
# 0~32767に変換
data = abs(data)
#PCM( = Sampling = 48000)
T_Flame = data.shape[0] #Total_Flame( = Sampling * Total_Time)
T_Time = T_Flame/PCM #Total_Time( = Total_Flame/PCM)

print("PCM sampling :",PCM,"Hz")
print("Total Flame :",T_Flame,"Flames")
print("Total Time:Total Flame/Sampling")
print(" = ",T_Time,"sec")

##np.arange(初項 = 初めの時間[sec], 
#           等差数列の終点　= 終わりの時間[sec], 
#           等差[sec])
time = np.arange(0, T_Time, Accuracy/PCM)

freq = 0

# Setting Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#Set Graph Title , Axis Label
ax.set_title("wav_3d",size=20)
ax.set_xlabel("Time[s]",size=15,color="black")
ax.set_ylabel("Loudness(bit)",size=15,color="black")
ax.set_zlabel("Frequency[Hz]",size=15,color="black")

#Down Sampling
data = data[::Accuracy]
#freq = freq[::Accuracy]

#Setting x,y,z
x = time
y = data
z = freq

#Data Plot
ax.scatter(x,y,z)
plt.show()