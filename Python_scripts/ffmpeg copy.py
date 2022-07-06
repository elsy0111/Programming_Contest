#実験用

#-----IMPORT-----#
import subprocess
#-----IMPORT-----#


list = [0,1,0,1,0,1]


#--------------Make Script for Terminal--------------#
n = 0
str_list = ""

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
		str_list += "-i audio/Sample_Audio/"+l+".wav "
		n += 1
#--------------Make Script for Terminal--------------#


#--------------Run on Terminal--------------#
script = "ffmpeg "+str_list+"-filter_complex "\
	'"[0]adelay=4800S|4800S[a];'\
	'[1]adelay=9600S|9600S[b];'\
	'[2]adelay=14400S|14400S[c];'\
	'[a][b][c]amix=' +str(n)+'" -y audio/Conposition_Audio/out.wav'
subprocess.run(script,shell = True)

time_script = 'ffmpeg -i audio/Conposition_Audio/out.wav -af "apad=whole_dur=10" audio/Conposition_Audio/time_out.wav'
subprocess.run(time_script,shell = True)
#--------------Run on Terminal--------------#


print("--------SCRIPT--------")
print(script)
print("--------SCRIPT--------")
print("--------SCRIPT--------")
print(time_script)
print("--------SCRIPT--------")