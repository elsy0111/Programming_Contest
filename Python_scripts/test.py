#自由、テスト、実験用。編集、削除可。

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

print(audio_str_list)
print()

delay_list = [4800,9600,14400]
delay_str_list = '"'
end_delay_str_list = ""
eng_str_list = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    delay_str_list += '[' + str(i) + "]adelay = " + str(delay_list[i]) + "S|" + str(delay_list[i]) + "S[" + eng_str_list[i] + "];"
    end_delay_str_list += "[" + eng_str_list[i] + "]"

delay_str_list += end_delay_str_list

script = "ffmpeg " + audio_str_list + "-filter_complex " + delay_str_list + 'amix=' +str(n)+'" -y audio/Conposition_Audio/out.wav'

print(script)