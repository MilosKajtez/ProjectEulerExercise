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
print(resultSequence)
result = 1000000
number = 999999
while(number > 500000):
    newSequence = getSequence(number)
    if(len(newSequence) > len(resultSequence)):
        resultSequence = newSequence
        result = number

    number -= 1
print(result)
            