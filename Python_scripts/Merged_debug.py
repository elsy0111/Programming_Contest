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


card_list = [   "あ・浅間のいたずら鬼の押出し",
                "い・伊香保温泉日本の名湯",
                "う・碓氷峠の関所跡",
                "え・縁起だるまの少林山",
                "お・太田金山子育呑龍",
                "か・関東と信越つなぐ高崎市",
                "き・桐生は日本の旗どころ",
                "く・草津よいとこ薬の温泉",
                "け・県都前橋生糸の市",
                "こ・心の塔台内村鑑三",
                "さ・三波石と共に名高い冬桜",
                "し・しのぶ毛の国二子塚",
                "す・裾野は長し赤城山",
                "せ・仙境尾瀬沼花の原",
                "そ・そろいの支度で八木節音頭",
                "た・滝は吹割片品渓谷",
                "ち・力あわせる二百万",
                "つ・つる舞う形の群馬県",
                "て・天下の義人茂左衛門",
                "と・利根は坂東一の川",
                "な・中仙道しのぶ安中杉並木",
                "に・日本で最初の富岡製糸",
                "ぬ・沼田城下の塩原太助",
                "ね・ねぎとこんにゃく下仁田名産",
                "の・登る榛名のキャンプ村",
                "は・花山公園つつじの名所",
                "ひ・白衣観音慈悲の御手",
                "ふ・分福茶釜の茂林寺",
                "へ・平和の使徒新島襄",
                "ほ・誇る文豪田山花袋",
                "ま・繭と生糸は日本一",
                "み・水上谷川スキーと登山",
                "む・昔を語る多胡の古碑",
                "め・銘仙織出す伊勢崎市",
                "も・紅葉に映える妙義山",
                "や・耶馬溪しのぐ吾妻峡",
                "ゆ・ゆかりは古し貫前神社",
                "よ・世のちり洗う四万温泉",
                "ら・雷と空風義理人情",
                "り・理想の電化に電源群馬",
                "る・ループで名高い清水トンネル",
                "れ・歴史に名高い新田義貞",
                "ろ・老農船津伝次平",
                "わ・和算の大家関孝和"]



#--------------Make Random List(length = 88)--------------#
# print()
# print('--------- start program ---------')

N = randint(3,5)#3-20
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
list = [0] * 88
for i in s_list:
    if i == 1:
        j = randint(0,1)
        if j == 1:
            list[cnt] = 1
            list[cnt + 1] = 0
        else:
            list[cnt] = 0
            list[cnt + 1] = 1
    cnt += 2

print("DATASET : ",list)

# print('------- end program [EOF] -------')
# print()
#--------------Make Random List(length = 88)--------------#

# f = open(str(t) + '.txt', 'w')

# f.write(str(t)+'\n')
# f.write("DATASET"+'\n')
# f.write(list+'\n')

#-------------------ここから合成---------------------#
#--------------Make Script for Terminal--------------#
out = 'audio/Conposition_Audio/out.wav'

n = 0
audio_str_list = ""


for i,j in enumerate(list):
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
		audio_str_list += "-i audio/Sample_Audio/"+l+".wav "
		n += 1

delay_list = []
for i in range(n):
    delay_list.append(randint(1,100000)) #ChangeThisssssssssssssssss

delay_str_list = '"'
end_delay_str_list = ""
eng_str_list = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    delay_str_list += '[' + str(i) + "]adelay = " + str(delay_list[i]) + "S|" + str(delay_list[i]) + "S[" + eng_str_list[i] + "];"
    end_delay_str_list += "[" + eng_str_list[i] + "]"

script = "ffmpeg " + audio_str_list + "-filter_complex " + delay_str_list + end_delay_str_list + 'amix=' +str(n)+'" -y ' + out

#--------------Make Script for Terminal--------------#



# f.write("Delay_List"+'\n')
# f.write(delay_list+'\n')
# f.write("FFmpeg Script"+'\n')
# f.write(script+'\n')


#--------------Run on Terminal--------------#
subprocess.run(script,shell = True)
#--------------Run on Terminal--------------#

print()
print("--------SCRIPT--------")
print(script)
print("--------SCRIPT--------")
print()

#-------------------ここまで合成---------------------#

#-------------------ここから分割---------------------#

n_split = 5 #Change Thisssssssssssssssssssssssss

wav_file_name = "audio/Conposition_Audio/out.wav"

pcm_n = librosa.get_samplerate(wav_file_name)

data,PCM = librosa.load(wav_file_name,sr = pcm_n)

frames = len(data)
sec = frames/PCM
c = True

print("frames :",frames)
print("PCM : ",PCM)
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


for j in range(n_split + 1):
    start_sample = split_list[j] + 1
    end_sample = split_list[j + 1]
    print(start_sample,end_sample)

    out = 'audio/Conposition_Audio/split/n_out_' + str(j + 1) + '.wav'

    script = "ffmpeg -y -i " + wav_file_name + " -af atrim=start_sample=" + str(start_sample) + ":end_sample=" + str(end_sample) + " " +  out

    subprocess.run(script,shell = True)
 
    #3sにそろえる
    time_script = 'ffmpeg -y -i ' + out + ' -af "apad=whole_dur=3" audio/Conposition_Audio/split/out_' + str(j + 1) + '.wav'
    subprocess.run(time_script,shell = True)

#-------------------ここまで分離---------------------#

plt.rcParams['font.family'] = "MS Gothic"

#--------------Set Parameter--------------#
fft_size = 2048                 # Frame length
hl = int(fft_size / 4)          # Frame shift length
hi = 512                        # Height of image
wi = 512                        # Width of image
F_max = 16000                   # Freq max
window = np.blackman(fft_size)  # Window Function
#--------------Set Parameter--------------#

plt.rcParams["figure.figsize"] = [10,8]
plt.rcParams["figure.autolayout"] = True

for j in range(n_split + 1):
    #--------------Make(Set) Empty Graph--------------#
    fig, ax = plt.subplots()
    #--------------Make(Set) Empty Graph--------------#

    #--------------Load Audio File--------------#
    wav_file_name = "audio/Conposition_Audio/split/out_" + str(j + 1) + ".wav"
    data, PCM = librosa.load(wav_file_name,sr = pcm_n)
    #--------------Load Audio File--------------#

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
    plt.savefig("images/Test/"+ str(t) + "_" + str(j + 1) + ".png")       # Change Thissssss
    #--------------Save Image--------------#





#--------------Set Parameter--------------#
fft_size = 2048                 # Frame length
hl = int(fft_size / 4)          # Frame shift length
hi = 512                        # Height of image
wi = 300                        # Width of image
F_max = 16000                   # Freq max
window = np.blackman(fft_size)  # Window Function
#--------------Set Parameter--------------#

#--------------Make(Set) Empty Graph--------------#
fig, ax = plt.subplots()
#--------------Make(Set) Empty Graph--------------#

#--------------Load Audio File--------------#
wav_file_name = "audio/Conposition_Audio/out.wav"
data, PCM = librosa.load(wav_file_name,sr = pcm_n)
#--------------Load Audio File--------------#

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
plt.savefig("images/Test/"+ str(t) + ".png")       # Change Thissssss
#--------------Save Image--------------#



#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#