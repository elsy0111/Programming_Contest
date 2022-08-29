from scipy.io.wavfile import read , write
import numpy as np

pcm,sample = read("audio/sample_Q_202205/sample_Q_202205/sample_Q_E01/sample_Q_E01/problem.wav")

nspeech = ['E01' , 'E02' , 'E03'] #重なった読みデータ数

#--------------MakeRandom------------------------
element_list = []
for i in nspeech:
    rater , datat = read("audio/Sample_Audio/"+i+".wav")
    element_list.append(len(datat))
#------------------------------------------------

#--------------max_sample_length---------------- 
new_list = sorted(element_list,reverse=True)

print(new_list)
print(element_list)

max_element = new_list[0]

print(max_element)
#------------------------------------------------

result = np.zeros(max_element)

for i,name in enumerate(nspeech):
    rater , datat = read("audio/Sample_Audio/"+name+".wav")
    print("element:"+str(len(datat)))
    pad_param = max_element-len(datat)
    print(pad_param)
    decoy = np.pad(datat,[0,pad_param])
    print(len(decoy))
    result += decoy

data_a = np.array(result,dtype=np.int16)
sample = np.array(sample,dtype=np.int16)
print(data_a)
print(len(sample))

f = open('myfile.txt', 'w')
f.write("data_a,sample\n")

for i in range(225000,226816):
    s = str(data_a[i])+" : "+str(sample[i]) 
    f.write(s+'\n')
f.close()