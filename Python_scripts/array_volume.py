from scipy.io.wavfile import read , write
import numpy as np

rate , data = read("/Users/sotarofurukawa/procon/Python_scripts/audio/Sample_Audio/E01.wav")
rate2 , data2 = read("/Users/sotarofurukawa/procon/Python_scripts/audio/Sample_Audio/E02.wav")
rate3 , data3 = read("/Users/sotarofurukawa/procon/Python_scripts/audio/Sample_Audio/E03.wav")
writefile = "/Users/sotarofurukawa/procon/Python_scripts/audio/test.wav"
rate4, data4 = read("/Users/sotarofurukawa/procon/Python_scripts/audio/sample_Q_202205/sample_Q_202205/sample_Q_E01/sample_Q_E01/problem.wav")

print(data)
print(data2)
print(data3)
print(len(data))
print(len(data2))
print(len(data3))

for i in range(8871):
    data=np.append(data,[0])

for i in range(51528):
    data3=np.append(data3,[0])
print(data.dtype)
data += data2 + data3
data_a = np.array(data,dtype=np.float64)
data_a /= 32768
write(writefile,rate=rate,data=data_a)
print(len(data_a))
print(len(data4))