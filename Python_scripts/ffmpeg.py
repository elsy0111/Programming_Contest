#-----時間計測用-----#
from time import time
start_time = time()
#-----時間計測用-----#


#-----IMPORT-----#
import subprocess
from random import randint
#-----IMPORT-----#


#--------------Make Random List(length = 88)--------------#
def make_random():
	# print()
	# print('--------- start program ---------')

	N = randint(3,20)
	print("N = ",N)

	t = []

	while len(t) < N:
		j = randint(1,44)
		t.append(j)
		#print(">>>",t)
		t = list(set(t))
		#print("del",t)
		#print()
	t.sort()

	print("t =",t)
	print("len(t) :",len(t))

	s_list = [0] * 44
	#print("empty s_list :\n",s_list)

	for i in t:
		s_list[i-1] = 1

	# print("set t in s_list :\n",s_list)
	# print("len(s_list) :",len(s_list))

	cnt = 0
	l_list = [0] * 88
	for i in s_list:
		if i == 1:
			j = randint(0,1)
			if j == 1:
				l_list[cnt] = 1
				l_list[cnt + 1] = 0
			else:
				l_list[cnt] = 0
				l_list[cnt + 1] = 1
		cnt += 2

	print(l_list)
	return(l_list)

	# print('------- end program [EOF] -------')
	# print()
#--------------Make Random List(length = 88)--------------#


#--------------本番用--------------#
# list = make_random()
#--------------本番用--------------#


#--------------Test Japanese--------------#
# 日本語計測用(J01-J20)
# list = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
#--------------Test Japanese--------------#


#--------------Test English--------------#
# 英語計測用(E01-E20)
list = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
#--------------Test English--------------#


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
script = "ffmpeg "+str_list+" -filter_complex amix="+str(n)+" -y audio/Conposition_Audio/out.wav"
subprocess.run(script,shell = True)
#--------------Run on Terminal--------------#


#--------------Audio Louder--------------#
# louder_script = "ffmpeg -i audio/Conposition_Audio/out.wav -filter:a volume=4 audio/Conposition_Audio/out_loud.wav"
# subprocess.run(louder_script,shell = True)
#--------------Audio Louder--------------#


print("--------SCRIPT--------")
print(script)
print("--------SCRIPT--------")

#-----時間計測用-----#
end_time = time()
print(end_time - start_time)
#-----時間計測用-----#