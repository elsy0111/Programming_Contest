from itertools import chain
from scipy.io.wavfile import read , write
import numpy as np
from random import randint


PCM,sample = read("audio/sample_Q_202205/sample_Q_202205/sample_Q_E01/sample_Q_E01/problem.wav")

audio_d_list = [0,1,0,1,0,1]

#--------------Make filename by audio_d_list-----------#
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
		n += 1
#--------------Make filename by audio_d_list-----------#






all_data = []
delay_list = []	#R^n
raw_audio_length_list = []

for i,name in enumerate(audio_list):
	PCM , data = read("audio/Sample_Audio/"+name+".wav")
	raw_audio_length_list.append(len(data))
	delay_random_num = randint(1,20000)	#Delay の 振れ幅ああ
	delay_list.append(delay_random_num)
	delay_empty_list = np.zeros(delay_random_num,dtype = int)
	all_data.append(list(chain(delay_empty_list,data)))

print("raw_audio_length \n",raw_audio_length_list)
print("delay \n",delay_list)

audio_length_list = []

for i in all_data:
    audio_length_list.append(len(i))

print("audio_length \n",audio_length_list)
raw_audio_length_list = np.array(raw_audio_length_list)
delay_list = np.array(delay_list)
print("raw_audio_length + delay_list \n",raw_audio_length_list + delay_list)





max_audio_length = max(audio_length_list)    

result = np.zeros(max_audio_length,dtype = int)

for data in all_data:
	n_empty = max_audio_length - len(data)
	empty_list = np.zeros(n_empty,dtype = int)
	long_data = list(chain(data,empty_list))
	result += long_data

print("result\n",result)
print("result audio length\n",len(result))

#-----------write txt------------
f = open('delete_debug.txt', 'w')

for i in range(len(sample)):	#len(sample) > len(result)
	s = str(sample[i]) + " , " + str(result[i])
	f.write(s + "\n")

f.close()
#-----------write txt------------


#--------------delete start end--------------
delete_list = []
for i in range(2):
	delete_list.append(randint(1,24000))

print("delete_list\n",delete_list)

result = result[:len(result) - delete_list[1]]
# print(len(result))
result = result[delete_list[0]:]
# print(len(result))
#--------------delete start end--------------

print("result",result)


result = np.array(result,dtype = float)
result /= 2**15

writefile = "audio/Conposition_Audio/out.wav"
write(writefile,rate = PCM,data = result)

