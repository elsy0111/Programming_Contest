#-----時間計測用-----#
from time import time
start_time = time()
#-----時間計測用-----#


#-----IMPORT-----#
from itertools import chain
from random import randint
import numpy as np
import librosa
from scipy.io.wavfile import read, write
#-----IMPORT-----#

f = open('audio/Conposition_Audio/meta_data.txt', 'w')

#--------------Make Random List(length = 88)--------------#
# N = randint(3,20)     #! No DEBUG
N = 5                   #! DEBUG
print("N = ",N)

t = []

while len(t) < N:
    j = randint(1,44)
    t.append(j)
    #print(">>>",t)
    t = list(set(t))
    #print("del",t)
    #print()
t.sort()

# print("t =",t)
# print("len(t) :",len(t))

s_list = [0] * 44
#print("empty s_list :\n",s_list)

for i in t:
    s_list[i-1] = 1

# print("set t in s_list :\n",s_list)
# print("len(s_list) :",len(s_list))

cnt = 0
list88 = [0] * 88
for i in s_list:
    if i == 1:
        j = randint(0,1)
        if j == 1:
            list88[cnt] = 1
            list88[cnt + 1] = 0
        else:
            list88[cnt] = 0
            list88[cnt + 1] = 1
    cnt += 2

#! DEBUG
list88 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("answer_label : ",list88)
#--------------Make Random List(length = 88)--------------#





#? out meta_data
f.write("合成データ数" + "\n" + str(N) + "\n")
f.write("合成元(目標値)" + "\n" + str(list88) + "\n")






#--------------Make filename by list88--------------#
out = 'audio/Conposition_Audio/out.wav'

#n_audio = N
n_audio = 0
audio_list = []


for i,j in enumerate(list88):
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
        n_audio += 1





#? out meta_data
f.write("合成元(種類)" + "\n" + str(audio_list) + "\n")





print("audio_list : ", audio_list)
#--------------Make filename by list88--------------#



#--------------Make delay_list--------------#
all_data = []
delay_list = []
raw_audio_length_list = []
delay_debug_list = [4800,9600,14400,19200,24000]   #! DEBUG

for i,name in enumerate(audio_list):
    PCM, data = read("audio/Sample_Audio/"+name+".wav")
    raw_audio_length_list.append(len(data))
    # delay_random_num = randint(0, 5) * 4800    #! random delay No DEBUG
    delay_random_num = delay_debug_list[i]      #! DEBUG
    delay_list.append(delay_random_num)
    cut_offset_data = data[delay_random_num:]
    all_data.append(cut_offset_data)
    
print("raw_audio_length_list : ", raw_audio_length_list)
print("delay_list : ", delay_list)

audio_length_list = []

for data in all_data:
    audio_length_list.append(len(data))

print("audio_length_list : ", audio_length_list)

raw_audio_length_list = np.array(raw_audio_length_list)
delay_list = np.array(delay_list)
print("raw_audio_length - delay_list : ", raw_audio_length_list - delay_list)
#--------------Make delay_list--------------#





#? out meta_data
f.write("Delay" + "\n" + str(delay_list) + "\n")





#------------------Fill Zreo----------------#
max_audio_length = max(audio_length_list)

result = np.zeros(max_audio_length,dtype = int)

for data in all_data:
    n_empty = max_audio_length - len(data)
    empty_list = np.zeros(n_empty,dtype = int)
    long_data = list(chain(data,empty_list))
    result += long_data

print("result : ", result)
print("max_audio_length : ", max_audio_length)
print("result_audio_length : ", len(result))
#------------------Fill Zreo----------------#


#n_split_audio = n_split + 1
n_split = randint(3,5) #! n_split


# """
#------------------Delete------------------#
""" # ! No DEBUG
while True:
    delete_num = randint(1,200000)
    if delete_num <= n_split * 0.65 * 48000:
        break
"""

delete_num = 0  #! DEBUG

print("delete_num : ", delete_num)

result = result[:len(result) - delete_num]
#------------------Delete------------------#
# """




#? out meta_data
f.write("冒頭,末尾削除" + "\n" + str(delete_num) + "\n")





print("result : ",result)
print("max_audio_length - sum(delete_list) : ",max_audio_length - delete_num)
print("len(result) : ",len(result))

#------------------Export audio----------------#
result = np.array(result,dtype = float)
result /= 2**15

writefile = "audio/Conposition_Audio/out.wav"
write(writefile,rate = PCM,data = result)
#------------------Export audio----------------#


wav_file_name = writefile

PCM = 48000

data,PCM = librosa.load(wav_file_name,sr = PCM)

frames = len(data)
sec = frames/PCM

print("frames : ",frames)
print("PCM : ",PCM)
print("SEC : ",sec)


#-----------------cut list------------------
c = True
while c:
    split_list = []
    for i in range(n_split):
        split_list.append(randint(1,frames))
    split_list.sort()
    split_list.insert(0,0)
    split_list.append(frames)
    c = False
    for i in range(n_split + 1):
        if split_list[i + 1] - split_list[i] <= 0.5 * 48000:
            c = True
#-----------------cut list------------------

#-----------------cut audio------------------
print("split list : ",split_list)




#? out meta_data
f.write("分割" + "\n" + str(split_list) + '\n')




split_list[-1] += 1
print("split_list : ",split_list)

for j in range(n_split + 1):
    split_data = data[split_list[j]:split_list[j + 1]]
    out = 'audio/Conposition_Audio/split/out_' + str(j + 1) + '.wav'
    write(out,rate = PCM,data = split_data)
#---------------------------Make Audio end-----------------------------#

f.close()

#! ------------- debug ----------------
#-----------write txt------------
PCM,sample = read("audio/sample_Q_202205/sample_Q_202205/sample_Q_J04/sample_Q_J04/problem.wav")
result *= 2**15

f = open('debug.txt', 'w')

for i in range(len(sample)):	#len(sample) > len(result)
	s = str(sample[i]) + " , " + str(int(result[i]))
	f.write(s + "\n")

print("frames: " , frames)
print("len(sample) = ", len(sample))
print("frames - len(sample) = ", frames - len(sample))

f.close()
#-----------write txt------------
#! ------------- debug ----------------

#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#
