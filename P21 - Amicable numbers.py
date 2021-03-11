result = 0

def sumOfDevisors(input):
    sum = 0
    for i in range(1, int(input/2) +1 ):
        if(input % i) == 0:
            sum += i
    return sum

for i in range(1, 10001):
    sumX = sumOfDevisors(i)

    if i == sumX:
        continue

    sumY = sumOfDevisors(sumX)

    if(sumY == i):
        result += i

print(result)