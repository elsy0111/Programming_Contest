from random import randint

print()
print('--------- start program ---------')

N = randint(3,20)
print("N = ",N)

t = []

while len(t) < N:
	j = randint(1,44)
	t.append(j)
	#print(">>>",t)
	t = list(set(t))
	#print("delete same number",t)
	#print()
t.sort()

print("t =",t)
print("len(t) :",len(t))

s_list = [0] * 44
print("empty s_list :\n",s_list)

for i in t:
	s_list[i-1] = 1

print("set t in s_list :\n",s_list)
print("len(s_list) :",len(s_list))

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
print("len(l_list) :",len(l_list))

print('------- end program [EOF] -------')