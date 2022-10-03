import numpy as np
"""
test(未完成)
n = 3
learning_list = [1,5,3,6,3,7,3,7,478,3,2,6,4]
"""
def make_answerlist(answer_list,n):
    result = []
    decoy = np.array(answer_list)
    result = decoy.argsort()[::-1]
    decoy = []
    for i in range(n):
        decoy.append(result[i])
    print(result)
    for i in range(len(decoy)):
        if decoy[i] % 2 == 0:
            decoy[i] /= 2
            decoy[i] += 1
        else:
            decoy[i] += 1
            decoy[i] /= 2
    print(decoy)
    result = map(int,list(set(decoy)))
    result = list(result)
    print(result)
    return result