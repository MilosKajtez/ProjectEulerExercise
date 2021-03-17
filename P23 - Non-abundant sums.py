largestPossible = 28123
abNums = []

def isAbundat(num):
    sumOfDevisor = 0
    for i in range(1, num):
        if(num%i == 0):
            sumOfDevisor += i
    return sumOfDevisor > num

for i in range(12,largestPossible):
    if isAbundat(i):
        abNums.append(i)

numbers = [x for x in range(0, largestPossible)]

for i in range(0,len(abNums)):
    for j in range(i, len(abNums)):
        if(abNums[i] + abNums[j])<largestPossible:
            numbers[abNums[i] + abNums[j]] = 0
        else:
            break
result = sum(numbers)

print(result )

