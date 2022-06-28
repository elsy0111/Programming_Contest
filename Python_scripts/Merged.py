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


#--------------Make(Set) Empty Graph--------------#
fig, ax = plt.subplots()
#--------------Make(Set) Empty Graph--------------#


for cnv in range(44):
    #--------------Make Script for Terminal--------------#
    n = 1
    cnv += 1
    if len(str(cnv)) == 1:
        l = "E0" + str(cnv) # Change Thissssss
    else:
        l = "E" + str(cnv)  # Change Thissssss
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
    img = librosa.display.specshow(data = S_dB, x_axis = 'time', y_axis = 'mel',
                                sr = PCM, fmax = F_max, ax = ax, cmap = "gray")
    #--------------Data Plot--------------#


    #--------------Save Image--------------#
    # plt.savefig("images/Mel_Spectrogram.png")
    # plt.savefig("images/Japanese_All/Mel_Spectrogram_"+l+".png") # Change Thissssss
    plt.savefig("images/English_All/Mel_Spectrogram_"+l+".png") # Change Thissssss
    #--------------Save Image--------------#


#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#