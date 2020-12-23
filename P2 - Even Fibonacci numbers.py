x = 1
y = 2
t = 0

result = 0

while y < 4000000:
    if (y % 2) == 0:
        result += y
    t = y
    y += x
    x = t
    

print("Result:", result)