number = 2
power = 1000

# get numer to a power and make it string
value = number ** power
asText = str(value)

result = 0

# add each char as int to result
for i in range(len(asText)):
    result += int(asText[i])

print(result)