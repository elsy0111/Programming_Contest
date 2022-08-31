from random import randint

l = []

for i in range(100):
    n = randint(0,5) * 4800
    l.append(n)

l = set(l)
l = sorted(l)
print(l)
