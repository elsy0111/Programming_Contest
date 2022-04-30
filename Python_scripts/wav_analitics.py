import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
 
 
#音声ファイル読み込み
wav_filename = "./audio/asano.wav"
rate, data = scipy.io.wavfile.read(wav_filename)

print("PCM sampling :",rate,data)
 
##### 音声データをそのまま表示する #####
#縦軸（振幅）の配列 = data   
# #16bitの音声ファイルのデータを-32768 から 32767にプロット

#横軸（時間）の配列 = time
##np.arange(初項, 等差数列の終点, 等差)
time = np.arange(0, data.shape[0]/rate, 1/rate)  
#データプロット
plt.plot(time, data)
plt.show()