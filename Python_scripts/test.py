import librosa

n_split = 4

wav_file_name = "audio/debug.mp3"

data,PCM = librosa.load(wav_file_name)

print(data)
print(len(data)/PCM)