import librosa
from random import randint

n_split = 4

wav_file_name = "Python_scripts/audio/Sample_Audio/E01.wav"

data,PCM = librosa.load(wav_file_name)

frames = len(data)
sec = frames/PCM
c = True

print("SEC : ",sec)

while c:
    split_list = []
    for i in range(n_split):
        split_list.append(randint(1,frames))
    split_list.sort()
    split_list.insert(0,1)
    split_list.append(frames)
    print("WHILE : ",split_list)
    c = False
    for i in range(n_split + 1):
        if split_list[i + 1] - split_list[i] <= 0.5 * 44100:
            c = True
print("final : ",split_list)