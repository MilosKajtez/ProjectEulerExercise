import math

num = 100

fac = math.factorial(100)

facStr = str(fac)

result = 0

for x in facStr:
    value = int(x)
    result += value
print (result)