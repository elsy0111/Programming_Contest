import subprocess
from random import randint

from time import time

start_time = time()

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
	# print("len(l_list) :",len(l_list))

	# print('------- end program [EOF] -------')



list = make_random()

n = 0
str_list = ""

for i,j in enumerate(list):
	i = int(i/2) + 1
	if j == 1:
		if i%2 != 0: #日本語
			if len(str(i)) == 1:
				l = "J0" + str(i)
			else:
				l = "J" + str(i)
		else:#英語
			if len(str(i)) == 1:
				l = "E0" + str(i)
			else:
				l = "E" + str(i)
		str_list += "-i audio/Sample_Audio/"+l+".wav "
		n += 1

print(str_list)

script = "ffmpeg "+str_list+" -filter_complex amix="+str(n)+" -y audio/Conposition_Audio/out.wav"

subprocess.run(script,shell = True)

# louder_script = "ffmpeg -i audio/Conposition_Audio/out.wav -filter:a volume=4 audio/Conposition_Audio/out_loud.wav"

# subprocess.run(louder_script,shell = True)

print(script)

end_time = time()

print(end_time - start_time)