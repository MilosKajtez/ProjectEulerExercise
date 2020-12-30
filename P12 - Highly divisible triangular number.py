import math

def getFactors(x):
    factors = []
    i = 1
    while i < math.sqrt(x):
        if((x%i)==0):
            if((x/i)==i):
                factors.append(i)
            else:
                factors.append(i)
                factors.append(x/i)
        i+=1
    return factors

result =0
i=1
ii = 1
while True:
    factors = getFactors(i)
    numberOfFactors = len(factors)
    if numberOfFactors > 500:
        result = i
        break
    ii +=1
    i = i + ii

print(result)