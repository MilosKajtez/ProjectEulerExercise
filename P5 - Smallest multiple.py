#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Check if number is prime number
def IsPrime(number):
    i =2
    while i < number:
        # If number is devidable( modulo is 0)  it's not prime
        if((number % i) == 0):
            return False
        i+=1
    return True

# Get next prime number
def getNextPrime(number):
    x = number
    while True:
        x += 1
        if(IsPrime(x)):
            return x


def getPrimeFactorization(x):
    primeFactors = []
    curent = x
    curentPrime = 2
    while curent != 1:
        # If prime is prime factor devide, add it to list and start from 2
        if ((curent % curentPrime) == 0):
            primeFactors.append(curentPrime)
            curent = curent / curentPrime
            curentPrime = 2
        else:
            # If prime is not prime factor, get next prime
            curentPrime = getNextPrime(curentPrime) 
    return primeFactors

allFactors = []
factors = []

# Get factorization for all numbers
for i in range(1,20):
    x = getPrimeFactorization(i)
    allFactors.append(x)
    factors.extend(x)

# Distinct factors
factors = list(set(factors))

result = 1

# Get maximum nnumber of repeats for each prime
# Multiplay primes to a power of repeats

for i in factors:
    highestCount = 0
    for ii in allFactors:
        count = ii.count(i)
        if(count > highestCount):
            highestCount = count
    result = result *  pow(i, highestCount)


print(result)