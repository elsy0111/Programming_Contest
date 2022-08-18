import librosa

wav_file_name = "audio\sample_Q_202205\sample_Q_202205\sample_Q_M01\sample_Q_M01\problem.wav"
n = librosa.get_samplerate(wav_file_name)
print(n)


data, PCM = librosa.load(wav_file_name,sr = n)

print(len(data),PCM)
print(len(data)/PCM)