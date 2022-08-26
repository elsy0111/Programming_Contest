from scipy.io.wavfile import read

rate , data = read("audio\sample_Q_202205\sample_Q_202205\sample_Q_M01\sample_Q_M01\problem.wav")

print(data)
print(len(data))