import subprocess
from tracemalloc import start
import librosa
from random import randint

n_split = 5 #Change Thisssssssssssssssssssssssss

wav_file_name = "audio/Conposition_Audio/out.wav"

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


for j in range(n_split + 1):
    start_sample = split_list[j] + 1
    end_sample = split_list[j + 1]
    print(start_sample,end_sample)

    out = 'audio/Conposition_Audio/split/out_' + str(j + 1) + '.wav'

    script = "ffmpeg -y -i " + wav_file_name + " -af atrim=start_sample=" + str(start_sample) + ":end_sample=" + str(end_sample) + " " +  out

    subprocess.run(script,shell = True)
    print(script)