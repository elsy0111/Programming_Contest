from itertools import chain
from scipy.io.wavfile import read , write
import numpy as np

#PCM not used

PCM,sample = read("audio/sample_Q_202205/sample_Q_202205/sample_Q_E01/sample_Q_E01/problem.wav")

audio_d_list = [0,1,0,1,0,1]

#--------------Make Script for Terminal--------------#
n = 0
audio_str_list = ""
audio_list = []

for i,j in enumerate(audio_d_list):
	if j == 1:
		if i%2 == 0: #日本語
			i = int(i/2) + 1
			if len(str(i)) == 1:
				l = "J0" + str(i)
			else:
				l = "J" + str(i)
		else:#英語
			i = int(i/2) + 1
			if len(str(i)) == 1:
				l = "E0" + str(i)
			else:
				l = "E" + str(i)
		audio_list.append(l)	
		audio_str_list += "-i audio/Sample_Audio/"+l+".wav "
		n += 1
#--------------Make Script for Terminal--------------#

audio_length_list = []

for i in audio_list:
    PCM , data = read("audio/Sample_Audio/"+i+".wav")
    audio_length_list.append(len(data))

max_audio_length = max(audio_length_list)    

result = np.zeros(max_audio_length,dtype = int)

for i,name in enumerate(audio_list):
	PCM , data = read("audio/Sample_Audio/"+name+".wav")
	n_empty = max_audio_length - len(data)
	empty_list = np.zeros(n_empty,dtype = int)
	long_data = list(chain(data,empty_list))
	result += long_data

# result /= 2**15

print(result)
print(sample)

f = open('array_volume_debug.txt', 'w')
f.write("sample - result" + "\n")

s3 = 0

for i in range(len(sample)):	#len(sample) > len(result)
	s = str(sample[i]) + " - " + str(result[i])
	s2 = str(sample[i] - result[i])
	s3 += int(s2)
	f.write(s + " = " + s2 + "\n")

f.write("sum entropy : " + str(s3))
f.close()