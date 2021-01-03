def getNexinSeqeuce(input):
    if((input % 2) == 0):
        return input/2
    else:
        return 3*input + 1

def getSequence(input):
    result = []
    x = input
    while x != 1:
        result.append(x)
        x = getNexinSeqeuce(x)
    result.append(1)
    return result

resultSequence = getSequence(1000000)
result = 1000000

for i in range(1,999999):
    print(i)
    newSequence = getSequence(i)
    if(len(newSequence) > len(resultSequence)):
        resultSequence = newSequence
        result = i

print(result)
            