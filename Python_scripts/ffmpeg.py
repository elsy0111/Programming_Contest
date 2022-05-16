import subprocess

list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

n = 0
str_list = ""
for i,j in enumerate(list):
	if j == 1:
		str_list += "-i audio/Sample_Audio/_"+str(i+1)+".wav "
		n += 1

script = "ffmpeg "+str_list+" -filter_complex amix="+str(n)+" -y audio/Conposition_Audio/out.wav"

subprocess.run(script,shell = True)

print(script)