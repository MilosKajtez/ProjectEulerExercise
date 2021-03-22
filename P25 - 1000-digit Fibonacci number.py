def countDigits(num):
    return len(str(num))

index = 2
x = 1
y = 1

while True:
    tmp = y
    y = x+y
    x = tmp
    index += 1
    if countDigits(y) == 1000:
        break

print(index)