#実験用

#-----IMPORT-----#
import subprocess
#-----IMPORT-----#


list = [0,1,0,1,0,1]


#--------------Make Script for Terminal--------------#
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
#--------------Make Script for Terminal--------------#


#--------------Run on Terminal--------------#
delay_list = [4800,9600,14400] #ここを変更
delay_str_list = '"'
end_delay_str_list = ""
eng_str_list = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    delay_str_list += '[' + str(i) + "]adelay = " + str(delay_list[i]) + "S|" + str(delay_list[i]) + "S[" + eng_str_list[i] + "];"
    end_delay_str_list += "[" + eng_str_list[i] + "]"

out = 'audio/Conposition_Audio/out.wav'

script = "ffmpeg " + audio_str_list + "-filter_complex " + delay_str_list + end_delay_str_list + 'amix=' +str(n)+'" -y ' + out
subprocess.run(script,shell = True)

#10sにそろえる
time_script = 'ffmpeg -i audio/Conposition_Audio/out.wav -af "apad=whole_dur=10" audio/Conposition_Audio/time_out.wav'
subprocess.run(time_script,shell = True)
#--------------Run on Terminal--------------#


print("--------SCRIPT--------")
print(script)
print("--------SCRIPT--------")
print("--------SCRIPT--------")
print(time_script)
print("--------SCRIPT--------")
