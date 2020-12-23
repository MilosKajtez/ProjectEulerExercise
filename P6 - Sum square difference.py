#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100

sumOfSqueres = 0
# Sum square of n + 1 (to include n)
for i in range(1,n + 1):
    sumOfSqueres += pow(i,2)

# square sum of n + 1 (to include n)
squareOfSum = pow(sum(range(n + 1)),2) 

result = squareOfSum - sumOfSqueres

print(result)