import string

# read file
file = open("Problem files\p022_names.txt","r")
namesRaw = file.read().split(",")
file.close()

names = []

# remove " from names and sort it
for name in namesRaw:
    names.append(name.replace("\"",""))

nameSorted = sorted(names)

# get sum of values for each name
# ord return int of a letter. a is 97 => ord(letter) - 96 = position in alphabet
def calculateAlphabeticValue(input):
    value = 0
    for i in range(0,len(input)):
        value += ord(input[i].lower()) -96
    return value

# Multiplay name value with index +1 [index is 0 based] and add it to sum
totalSum = 0
for i in range(0,len(nameSorted)):
    totalSum += (i +1 ) * calculateAlphabeticValue(nameSorted[i])

print(totalSum)
