longest = 1
result = 1

def cycleLength(number):
    for i in range(1,number):
        if(1 == 10**i % number):
            return i
    return 0

for i in range(1,1001):
    current = cycleLength(i)
    if(current > longest):
        longest = current
        result = i

print(result)