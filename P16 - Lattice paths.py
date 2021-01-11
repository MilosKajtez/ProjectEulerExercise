import math

x,y = 20

# Calculate binomial for
# x + y
#   x

res =int( math.factorial((x+y)) /( math.factorial(y)* math.factorial(y)))

print(res)