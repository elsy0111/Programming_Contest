#-----時間計測用-----#
from time import time
start_time = time()
#-----時間計測用-----#


#-----IMPORT-----#
import subprocess
from random import randint
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
#-----IMPORT-----#

#--------------Make Random List(length = 88)--------------#
# print()
# print('--------- start program ---------')

N = randint(2,3)
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

print("t =",t)
print("len(t) :",len(t))

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

# print('------- end program [EOF] -------')
# print()
#--------------Make Random List(length = 88)--------------#



#--------------Make filename by list88--------------#
out = 'audio/Conposition_Audio/out.wav'

n_audio = 0
audio_list = ""


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
#--------------Make delay_list--------------#



plt.rcParams['font.family'] = "MS Gothic"

#--------------Make(Set) Empty Graph--------------#
fig, ax = plt.subplots()
#--------------Make(Set) Empty Graph--------------#

#--------------Load Audio File--------------#
wav_file_name = "audio\Conposition_Audio\\time_out.wav"
data, PCM = librosa.load(wav_file_name)
#--------------Load Audio File--------------#


#--------------Set Parameter--------------#
fft_size = 2048                 # Frame length
hl = int(fft_size / 4)          # Frame shift length
hi = 300                        # Height of image
wi = 300                        # Width of image
F_max = 20000                   # Freq max
window = np.blackman(fft_size)  # Window Function
#--------------Set Parameter--------------#


plt.rcParams["figure.figsize"] = [20, 10]
plt.rcParams["figure.autolayout"] = True
data = data[0:wi*hl]


#--------------STFT--------------#
S = librosa.feature.melspectrogram(
    y = data, sr = PCM, n_mels = hi, fmax = F_max, hop_length = hl, 
    win_length = fft_size, n_fft = fft_size, window = window)

S_dB = librosa.power_to_db(S, ref = np.max)
#--------------STFT--------------#


#--------------Data Plot--------------#
plt.title(str(t))
img = librosa.display.specshow(data = S_dB, x_axis = 'time', y_axis = 'mel',
                            sr = PCM, fmax = F_max, ax = ax, cmap = "gray")
#--------------Data Plot--------------#


#--------------Save Image--------------#
# plt.savefig("images/Mel_Spectrogram.png")
# plt.savefig("images/Japanese_All/Mel_Spectrogram_"+l+".png")      # Change Thissssss
plt.savefig("images/Test/"+str(t)+".png")       # Change Thissssss
#--------------Save Image--------------#


#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#