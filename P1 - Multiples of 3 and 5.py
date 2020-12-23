maxNummber = 1000
result = 0

for i in range(maxNummber):
    if ((i % 3) == 0) or ((i % 5) == 0):
        result += i 

print("Result:", result)