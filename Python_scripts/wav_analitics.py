import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
 
 
#音声ファイル読み込み
wav_filename = "./audio/asano.wav"
rate, data = scipy.io.wavfile.read(wav_filename)

PCM = rate
T_Flame = data.shape[0]
T_Time = T_Flame/rate

print("PCM sampling :",PCM,"Hz")
print("Total Flame :",T_Flame,"Flames")
print("Total Time:Total Flame/Sampling")
print(" = ",T_Time,"sec")

##### 音声データをそのまま表示する #####
#縦軸（振幅）の配列 = data   
# #16bitの音声ファイルのデータを-32768 から 32767にプロット

#横軸（時間）の配列 = time
##np.arange(初項 = 初めの時間[sec], 
#           等差数列の終点　= 終わりの時間[sec], 
#           等差[sec])
time = np.arange(0, T_Time, 1/PCM)

plt.xlabel("Time[s]")
plt.ylabel("Loudness(bit)")

#データプロット
plt.plot(time, data)
plt.show()