#-----時間計測用-----#
from time import time
start_time = time()
#-----時間計測用-----#


#-----IMPORT-----#
from itertools import chain
from random import randint
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
import subprocess
#-----IMPORT-----#

#--------------Make Random List(length = 88)--------------#
N = randint(3,20)
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

print("answer_label : ",list88)
#--------------Make Random List(length = 88)--------------#



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
#--------------Make filename by list88--------------#



#--------------Make delay_list--------------#
all_data = []
delay_list = []
raw_audio_length_list = []

for i,name in enumerate(audio_list):
    PCM, data = read("audio/Sample_Audio/"+name+".wav")
    raw_audio_length_list.append(len(data))
    delay_random_num = randint(1, 20000)    #random delay
    delay_list.append(delay_random_num)
    delay_empty_list= np.zeros(delay_random_num, dtype = int)
    all_data.append(list(chain(delay_empty_list, data)))
    
print("raw_audio_length_list : ", raw_audio_length_list)
print("delay_list : ", delay_list)

audio_length_list = []

for data in all_data:
    audio_length_list.append(len(data))

print("audio_length_list : ", audio_length_list)

raw_audio_length_list = np.array(raw_audio_length_list)
delay_list = np.array(delay_list)
print("raw_audio_length + delay_list : ", raw_audio_length_list + delay_list)
#--------------Make delay_list--------------#


#------------------Fill Zreo----------------#
max_audio_length = max(audio_length_list)

result = np.zeros(max_audio_length,dtype = int)

for data in all_data:
    n_empty = max_audio_length - len(data)
    empty_list = np.zeros(n_empty,dtype = int)
    long_data = list(chain(data,empty_list))
    result += long_data

print("result : ", result)
print("result_audio_length : ", len(result))
#------------------Fill Zreo----------------#

#------------------Delete start end------------------#
delete_list = []
for i in range(2):
    delete_list.append(randint(1,24000))

print("delete_list : ", delete_list)

result = result[:len(result) - delete_list[1]]
result = result[delete_list[0]:]
#------------------Delete start end------------------#

print("result : ",result)
print("len(result) : ",len(result))

#------------------Export audio----------------#
result = np.array(result,dtype = float)
result /= 2**15

writefile = "audio/Conposition_Audio/out.wav"
write(writefile,rate = PCM,data = result)
#------------------Export audio----------------#

#n_split_audio = n_split + 1
n_split = randint(3,5) #Change Thisssssssssssssssssssssssss

wav_file_name = writefile

n = librosa.get_samplerate(wav_file_name)

data,PCM = librosa.load(wav_file_name,sr = n)

frames = len(data)
sec = frames/PCM
c = True

print(frames)
print(PCM)
print("SEC : ",sec)

while c:
    split_list = []
    for i in range(n_split):
        split_list.append(randint(1,frames))
    split_list.sort()
    split_list.insert(0,0)
    split_list.append(frames)
    print("WHILE : ",split_list)
    c = False
    for i in range(n_split + 1):
        if split_list[i + 1] - split_list[i] <= 0.5 * 48000:
            c = True
print("final : ",split_list)
#-----------------cut list------------------



#-----------------cut audio------------------
for j in range(n_split + 1):
    start_sample = split_list[j] + 1
    end_sample = split_list[j + 1]
    print(start_sample,end_sample)

    out = 'audio/Conposition_Audio/split/out_' + str(j + 1) + '.wav'

    script = "ffmpeg -y -i " + wav_file_name + " -af atrim=start_sample=" + str(start_sample) + ":end_sample=" + str(end_sample) + " " +  out

    subprocess.run(script,shell = True)
    print(script)
#-----------------cut audio------------------

#---------------------------Make Audio end-----------------------------#

#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#
