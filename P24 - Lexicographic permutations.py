from itertools import permutations

t = permutations([0,1,2,3,4,5,6,7,8,9])
k = 0
for i in t:
    k += 1
    if k == 1000000:
        print(i)


    