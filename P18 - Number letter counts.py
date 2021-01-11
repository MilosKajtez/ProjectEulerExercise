import math

values = {
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6,
    100:7,
    1000:8
}
    


def getCharCount(x):
    charCount = 0
    workingNumber = x

    if(workingNumber > 999):
        thousands = math.floor(workingNumber/1000)*1000
        numberOfThousands = thousands / 1000
        charCount += values.get(numberOfThousands)
        charCount += values.get(1000)
        workingNumber -= thousands
    
    if(workingNumber > 99):
        hundreds = math.floor(workingNumber/100)*100
        numberOfHundreds = hundreds / 100
        charCount += values.get(numberOfHundreds)
        charCount += values.get(100)
        
        workingNumber -= hundreds
        if(workingNumber != 0):
            charCount += 3 # add 3 for and

    if(workingNumber > 20):
        tens = math.floor(workingNumber/10)*10
        charCount += values.get(tens)
        workingNumber -= tens
    
    if(workingNumber != 0):
        charCount += values.get(workingNumber)

    return charCount


result = 0
maxNum = 1000

for i in range(1, maxNum +1):
    charCount = getCharCount(i)
    result += charCount

print(result)