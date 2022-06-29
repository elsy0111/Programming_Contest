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

plt.rcParams['font.family'] = "MS Gothic"

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


#--------------Make(Set) Empty Graph--------------#
fig, ax = plt.subplots()
#--------------Make(Set) Empty Graph--------------#


for cnv in range(44):
    #--------------Make Script for Terminal--------------#
    n = 1
    cnv += 1
    if len(str(cnv)) == 1:
        l = "E0" + str(cnv)     # Change Thissssss
    else:
        l = "E" + str(cnv)      # Change Thissssss
    str_list = "-i audio/Sample_Audio/"+l+".wav "
    #--------------Make Script for Terminal--------------#


    #--------------Run on Terminal--------------#
    script = "ffmpeg "+str_list+" -filter_complex amix="+str(n)+" -y audio/Conposition_Audio/out.wav"
    subprocess.run(script,shell = True)
    #--------------Run on Terminal--------------#


    print()
    print("--------SCRIPT--------")
    print(script)
    print("--------SCRIPT--------")
    print()


    #--------------Load Audio File--------------#
    wav_file_name = "audio\Conposition_Audio\out.wav"
    data, PCM = librosa.load(wav_file_name)
    #--------------Load Audio File--------------#


    #--------------Set Parameter--------------#
    fft_size = 2048                 # Frame length
    hl = int(fft_size / 4)          # Frame shift length
    hi = 512                        # Height of image
    wi = 256                        # Width of image
    F_max = 10000                   # Freq max
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
    plt.title(l+str(card_list[cnv-1]))
    img = librosa.display.specshow(data = S_dB, x_axis = 'time', y_axis = 'mel',
                                sr = PCM, fmax = F_max, ax = ax, cmap = "gray")
    #--------------Data Plot--------------#


    #--------------Save Image--------------#
    # plt.savefig("images/Mel_Spectrogram.png")
    # plt.savefig("images/Japanese_All/Mel_Spectrogram_"+l+".png")      # Change Thissssss
    plt.savefig("images/English_All/Mel_Spectrogram_"+l+".png")       # Change Thissssss
    #--------------Save Image--------------#


#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#